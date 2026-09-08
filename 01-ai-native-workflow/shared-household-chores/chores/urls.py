from django.urls import path

from . import views

urlpatterns = [
    path("", views.chore_list, name="chore-list"),
    path("completed/", views.completed_chores, name="completed-chores"),
    path("chores/new/", views.chore_create, name="chore-create"),
    path("chores/<int:pk>/edit/", views.chore_edit, name="chore-edit"),
    path("chores/<int:pk>/complete/", views.chore_complete, name="chore-complete"),
    path("members/new/", views.member_create, name="member-create"),
]
