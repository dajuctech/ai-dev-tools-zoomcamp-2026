from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

from .forms import ChoreForm, HouseholdMemberForm
from .models import Chore, HouseholdMember


def chore_list(request):
    chores = Chore.objects.filter(status=Chore.Status.PENDING).select_related("assignee")
    members = HouseholdMember.objects.all()
    return render(
        request,
        "chores/chore_list.html",
        {
            "chores": chores,
            "members": members,
            "member_form": HouseholdMemberForm(),
        },
    )


def completed_chores(request):
    chores = Chore.objects.filter(status=Chore.Status.COMPLETE).select_related("assignee")
    return render(request, "chores/completed_chores.html", {"chores": chores})


def chore_create(request):
    if request.method == "POST":
        form = ChoreForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Chore created.")
            return redirect("chore-list")
    else:
        form = ChoreForm()
    return render(request, "chores/chore_form.html", {"form": form, "title": "New Chore"})


def chore_edit(request, pk):
    chore = get_object_or_404(Chore, pk=pk)
    if request.method == "POST":
        form = ChoreForm(request.POST, instance=chore)
        if form.is_valid():
            form.save()
            messages.success(request, "Chore updated.")
            return redirect("chore-list")
    else:
        form = ChoreForm(instance=chore)
    return render(request, "chores/chore_form.html", {"form": form, "title": "Edit Chore"})


@require_POST
def chore_complete(request, pk):
    chore = get_object_or_404(Chore, pk=pk)
    chore.mark_complete()
    messages.success(request, "Chore completed.")
    return redirect("chore-list")


@require_POST
def member_create(request):
    form = HouseholdMemberForm(request.POST)
    if form.is_valid():
        form.save()
        messages.success(request, "Household member added.")
    else:
        messages.error(request, "Enter a unique household member name.")
    return redirect("chore-list")
