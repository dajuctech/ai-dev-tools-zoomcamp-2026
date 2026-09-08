from django.conf import settings
from django.db import models


class Project(models.Model):
    name = models.CharField(max_length=160)
    facilitator = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="facilitated_projects",
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["name"]

    def __str__(self) -> str:
        return self.name


class Membership(models.Model):
    class Role(models.TextChoices):
        MEMBER = "member", "Team member"
        FACILITATOR = "facilitator", "Facilitator"

    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="memberships")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="memberships")
    role = models.CharField(max_length=20, choices=Role.choices, default=Role.MEMBER)

    class Meta:
        unique_together = ["project", "user"]

    def __str__(self) -> str:
        return f"{self.user} in {self.project}"


class FeedbackCycle(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="cycles")
    title = models.CharField(max_length=160)
    is_open = models.BooleanField(default=True)
    is_revealed = models.BooleanField(default=False)
    voting_closed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self) -> str:
        return f"{self.project}: {self.title}"


class Cluster(models.Model):
    cycle = models.ForeignKey(FeedbackCycle, on_delete=models.CASCADE, related_name="clusters")
    title = models.CharField(max_length=160)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["title"]

    def vote_total(self) -> int:
        return sum(vote.count for vote in self.votes.all())

    def __str__(self) -> str:
        return self.title


class FeedbackItem(models.Model):
    class Category(models.TextChoices):
        START = "start", "Start"
        STOP = "stop", "Stop"
        CONTINUE = "continue", "Continue"

    cycle = models.ForeignKey(FeedbackCycle, on_delete=models.CASCADE, related_name="feedback_items")
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="feedback_items")
    category = models.CharField(max_length=20, choices=Category.choices)
    body = models.TextField()
    is_anonymous = models.BooleanField(default=False)
    cluster = models.ForeignKey(
        Cluster,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="feedback_items",
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["category", "created_at"]

    def visible_author(self) -> str:
        if self.is_anonymous:
            return "Anonymous"
        display = self.author.first_name.strip()
        return display or self.author.username

    def __str__(self) -> str:
        return f"{self.get_category_display()}: {self.body[:40]}"


class Vote(models.Model):
    cycle = models.ForeignKey(FeedbackCycle, on_delete=models.CASCADE, related_name="votes")
    cluster = models.ForeignKey(Cluster, on_delete=models.CASCADE, related_name="votes")
    voter = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="votes")
    count = models.PositiveSmallIntegerField(default=1)

    class Meta:
        unique_together = ["cluster", "voter"]

    def __str__(self) -> str:
        return f"{self.voter} -> {self.cluster} ({self.count})"


class Decision(models.Model):
    cycle = models.ForeignKey(FeedbackCycle, on_delete=models.CASCADE, related_name="decisions")
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_at"]

    def __str__(self) -> str:
        return self.text[:60]


class ActionItem(models.Model):
    cycle = models.ForeignKey(FeedbackCycle, on_delete=models.CASCADE, related_name="action_items")
    description = models.TextField()
    owner = models.CharField(max_length=120)
    due_date = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_at"]

    def __str__(self) -> str:
        return self.description[:60]


class TranscriptProcessing(models.Model):
    cycle = models.ForeignKey(FeedbackCycle, on_delete=models.CASCADE, related_name="transcript_runs")
    transcript = models.TextField()
    extracted_notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self) -> str:
        return f"Transcript for {self.cycle}"
