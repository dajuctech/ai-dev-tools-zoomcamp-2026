from django.contrib import admin

from .models import Chore, HouseholdMember


@admin.register(HouseholdMember)
class HouseholdMemberAdmin(admin.ModelAdmin):
    list_display = ["name", "created_at"]
    search_fields = ["name"]


@admin.register(Chore)
class ChoreAdmin(admin.ModelAdmin):
    list_display = ["title", "assignee", "due_date", "status", "completed_at"]
    list_filter = ["status", "due_date"]
    search_fields = ["title", "description", "assignee__name"]
