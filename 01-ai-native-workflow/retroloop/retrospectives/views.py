from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.db.models import Prefetch, Sum
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

from .forms import (
    ActionItemForm,
    ClusterForm,
    DecisionForm,
    FeedbackCycleForm,
    FeedbackItemForm,
    ProjectForm,
    RegistrationForm,
    TranscriptForm,
)
from .models import ActionItem, Cluster, Decision, FeedbackCycle, FeedbackItem, Membership, Project, Vote
from .services import cast_vote, ensure_default_clusters, process_transcript


def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("project-list")
    else:
        form = RegistrationForm()
    return render(request, "registration/register.html", {"form": form})


@login_required
def project_list(request):
    projects = Project.objects.filter(memberships__user=request.user).distinct()
    return render(request, "retrospectives/project_list.html", {"projects": projects})


@login_required
def project_create(request):
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.facilitator = request.user
            project.save()
            Membership.objects.create(project=project, user=request.user, role=Membership.Role.FACILITATOR)
            messages.success(request, "Project created.")
            return redirect("project-detail", pk=project.pk)
    else:
        form = ProjectForm()
    return render(request, "retrospectives/project_form.html", {"form": form})


@login_required
def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    cycles = project.cycles.all()
    return render(request, "retrospectives/project_detail.html", {"project": project, "cycles": cycles})


@login_required
def cycle_create(request, project_pk):
    project = get_object_or_404(Project, pk=project_pk)
    if request.method == "POST":
        form = FeedbackCycleForm(request.POST)
        if form.is_valid():
            cycle = form.save(commit=False)
            cycle.project = project
            cycle.save()
            messages.success(request, "Feedback cycle created.")
            return redirect("cycle-detail", pk=cycle.pk)
    else:
        form = FeedbackCycleForm()
    return render(request, "retrospectives/cycle_form.html", {"form": form, "project": project})


@login_required
def cycle_detail(request, pk):
    cycle = get_object_or_404(FeedbackCycle.objects.select_related("project"), pk=pk)
    if cycle.is_revealed:
        feedback = cycle.feedback_items.select_related("author", "cluster")
    else:
        feedback = cycle.feedback_items.filter(author=request.user).select_related("author", "cluster")
    return render(request, "retrospectives/cycle_detail.html", {"cycle": cycle, "feedback": feedback})


@login_required
def feedback_create(request, cycle_pk):
    cycle = get_object_or_404(FeedbackCycle.objects.select_related("project"), pk=cycle_pk)
    if request.method == "POST":
        form = FeedbackItemForm(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.cycle = cycle
            item.author = request.user
            item.save()
            messages.success(request, "Feedback submitted.")
            return redirect("cycle-detail", pk=cycle.pk)
    else:
        form = FeedbackItemForm()
    return render(request, "retrospectives/feedback_form.html", {"form": form, "cycle": cycle})


@login_required
def board(request, cycle_pk):
    cycle = get_object_or_404(FeedbackCycle.objects.select_related("project"), pk=cycle_pk)
    clusters = list(
        cycle.clusters.prefetch_related(
            Prefetch("feedback_items", queryset=FeedbackItem.objects.select_related("author")),
            "votes",
        )
        .all()
    )
    totals = {
        item["cluster"]: item["total"] or 0
        for item in Vote.objects.filter(cycle=cycle).values("cluster").annotate(total=Sum("count"))
    }
    cluster_rows = [{"cluster": cluster, "total": totals.get(cluster.pk, 0)} for cluster in clusters]
    user_votes = Vote.objects.filter(cycle=cycle, voter=request.user).aggregate(total=Sum("count"))["total"] or 0
    unclustered = cycle.feedback_items.filter(cluster__isnull=True).select_related("author")
    return render(
        request,
        "retrospectives/board.html",
        {
            "cycle": cycle,
            "clusters": clusters,
            "cluster_rows": cluster_rows,
            "user_votes": user_votes,
            "votes_left": max(0, 3 - user_votes),
            "unclustered": unclustered,
            "cluster_form": ClusterForm(),
        },
    )


@login_required
@require_POST
def reveal_feedback(request, cycle_pk):
    cycle = get_object_or_404(FeedbackCycle, pk=cycle_pk)
    cycle.is_revealed = True
    cycle.is_open = False
    cycle.save(update_fields=["is_revealed", "is_open"])
    ensure_default_clusters(cycle)
    messages.success(request, "Feedback revealed.")
    return redirect("board", cycle_pk=cycle.pk)


@login_required
@require_POST
def cluster_create(request, cycle_pk):
    cycle = get_object_or_404(FeedbackCycle, pk=cycle_pk)
    form = ClusterForm(request.POST)
    if form.is_valid():
        cluster = form.save(commit=False)
        cluster.cycle = cycle
        cluster.save()
        messages.success(request, "Cluster added.")
    return redirect("board", cycle_pk=cycle.pk)


@login_required
@require_POST
def cluster_rename(request, cluster_pk):
    cluster = get_object_or_404(Cluster.objects.select_related("cycle"), pk=cluster_pk)
    form = ClusterForm(request.POST, instance=cluster)
    if form.is_valid():
        form.save()
        messages.success(request, "Cluster renamed.")
    return redirect("board", cycle_pk=cluster.cycle.pk)


@login_required
@require_POST
def feedback_move(request, item_pk):
    item = get_object_or_404(FeedbackItem.objects.select_related("cycle"), pk=item_pk)
    cluster_id = request.POST.get("cluster")
    item.cluster = get_object_or_404(Cluster, pk=cluster_id, cycle=item.cycle) if cluster_id else None
    item.save(update_fields=["cluster"])
    messages.success(request, "Feedback moved.")
    return redirect("board", cycle_pk=item.cycle.pk)


@login_required
@require_POST
def vote(request, cluster_pk):
    cluster = get_object_or_404(Cluster.objects.select_related("cycle"), pk=cluster_pk)
    if cast_vote(cluster.cycle, cluster, request.user):
        messages.success(request, "Vote recorded.")
    else:
        messages.error(request, "No votes left or voting is closed.")
    return redirect("board", cycle_pk=cluster.cycle.pk)


@login_required
@require_POST
def close_voting(request, cycle_pk):
    cycle = get_object_or_404(FeedbackCycle, pk=cycle_pk)
    cycle.voting_closed = True
    cycle.save(update_fields=["voting_closed"])
    messages.success(request, "Voting closed.")
    return redirect("board", cycle_pk=cycle.pk)


@login_required
def summary(request, cycle_pk):
    cycle = get_object_or_404(FeedbackCycle.objects.select_related("project"), pk=cycle_pk)
    if request.method == "POST":
        if "decision" in request.POST:
            form = DecisionForm(request.POST, prefix="decision")
            if form.is_valid():
                decision = form.save(commit=False)
                decision.cycle = cycle
                decision.save()
                messages.success(request, "Decision added.")
                return redirect("summary", cycle_pk=cycle.pk)
        elif "action" in request.POST:
            form = ActionItemForm(request.POST, prefix="action")
            if form.is_valid():
                action = form.save(commit=False)
                action.cycle = cycle
                action.save()
                messages.success(request, "Action item added.")
                return redirect("summary", cycle_pk=cycle.pk)

    return render(
        request,
        "retrospectives/summary.html",
        {
            "cycle": cycle,
            "decisions": Decision.objects.filter(cycle=cycle),
            "action_items": ActionItem.objects.filter(cycle=cycle),
            "decision_form": DecisionForm(prefix="decision"),
            "action_form": ActionItemForm(prefix="action"),
        },
    )


@login_required
def transcript_upload(request, cycle_pk):
    cycle = get_object_or_404(FeedbackCycle.objects.select_related("project"), pk=cycle_pk)
    result = None
    if request.method == "POST":
        form = TranscriptForm(request.POST)
        if form.is_valid():
            result = process_transcript(cycle, form.cleaned_data["transcript"])
            messages.success(request, "Transcript processed.")
    else:
        form = TranscriptForm()
    return render(request, "retrospectives/transcript_upload.html", {"cycle": cycle, "form": form, "result": result})
