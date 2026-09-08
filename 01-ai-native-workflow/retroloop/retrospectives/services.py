from django.db.models import Sum

from .models import ActionItem, Cluster, Decision, FeedbackCycle, FeedbackItem, TranscriptProcessing, Vote


def ensure_default_clusters(cycle: FeedbackCycle) -> None:
    labels = {
        FeedbackItem.Category.START: "Start",
        FeedbackItem.Category.STOP: "Stop",
        FeedbackItem.Category.CONTINUE: "Continue",
    }
    clusters = {}
    for category, title in labels.items():
        cluster, _ = Cluster.objects.get_or_create(cycle=cycle, title=title)
        clusters[category] = cluster

    for item in cycle.feedback_items.filter(cluster__isnull=True):
        item.cluster = clusters[item.category]
        item.save(update_fields=["cluster"])


def cast_vote(cycle: FeedbackCycle, cluster: Cluster, voter) -> bool:
    if cycle.voting_closed:
        return False
    total_votes = Vote.objects.filter(cycle=cycle, voter=voter).aggregate(total=Sum("count"))["total"] or 0
    if total_votes >= 3:
        return False
    vote, _ = Vote.objects.get_or_create(cycle=cycle, cluster=cluster, voter=voter, defaults={"count": 0})
    vote.count += 1
    vote.save(update_fields=["count"])
    return True


def process_transcript(cycle: FeedbackCycle, transcript: str) -> TranscriptProcessing:
    notes: list[str] = []
    for raw_line in transcript.splitlines():
        line = raw_line.strip()
        lowered = line.lower()
        if not line:
            continue
        if lowered.startswith("decision:") or "decided" in lowered:
            text = line.split(":", 1)[-1].strip() if ":" in line else line
            Decision.objects.create(cycle=cycle, text=text)
            notes.append(f"Decision: {text}")
        elif lowered.startswith("action:") or lowered.startswith("todo:"):
            text = line.split(":", 1)[-1].strip() if ":" in line else line
            ActionItem.objects.create(cycle=cycle, description=text, owner="Unassigned")
            notes.append(f"Action: {text}")

    extracted_notes = "\n".join(notes) if notes else "No candidate decisions or actions found."
    return TranscriptProcessing.objects.create(
        cycle=cycle,
        transcript=transcript,
        extracted_notes=extracted_notes,
    )
