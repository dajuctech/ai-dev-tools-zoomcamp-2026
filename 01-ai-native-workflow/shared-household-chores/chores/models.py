from django.db import models
from django.utils import timezone


class HouseholdMember(models.Model):
    name = models.CharField(max_length=120, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["name"]

    def __str__(self) -> str:
        return self.name


class Chore(models.Model):
    class Status(models.TextChoices):
        PENDING = "pending", "Pending"
        COMPLETE = "complete", "Complete"

    title = models.CharField(max_length=160)
    description = models.TextField(blank=True)
    assignee = models.ForeignKey(
        HouseholdMember,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="chores",
    )
    due_date = models.DateField(blank=True, null=True)
    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.PENDING,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    completed_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        ordering = ["status", "due_date", "created_at"]

    def __str__(self) -> str:
        return self.title

    @property
    def is_complete(self) -> bool:
        return self.status == self.Status.COMPLETE

    def mark_complete(self) -> None:
        if not self.completed_at:
            self.completed_at = timezone.now()
        self.status = self.Status.COMPLETE
        self.save(update_fields=["status", "completed_at"])
