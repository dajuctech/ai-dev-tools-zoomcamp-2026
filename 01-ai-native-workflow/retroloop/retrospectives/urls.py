from django.urls import path

from . import views

urlpatterns = [
    path("", views.project_list, name="project-list"),
    path("register/", views.register, name="register"),
    path("projects/new/", views.project_create, name="project-create"),
    path("projects/<int:pk>/", views.project_detail, name="project-detail"),
    path("projects/<int:project_pk>/cycles/new/", views.cycle_create, name="cycle-create"),
    path("cycles/<int:pk>/", views.cycle_detail, name="cycle-detail"),
    path("cycles/<int:cycle_pk>/feedback/new/", views.feedback_create, name="feedback-create"),
    path("cycles/<int:cycle_pk>/board/", views.board, name="board"),
    path("cycles/<int:cycle_pk>/reveal/", views.reveal_feedback, name="reveal-feedback"),
    path("cycles/<int:cycle_pk>/clusters/new/", views.cluster_create, name="cluster-create"),
    path("cycles/<int:cycle_pk>/voting/close/", views.close_voting, name="close-voting"),
    path("cycles/<int:cycle_pk>/summary/", views.summary, name="summary"),
    path("cycles/<int:cycle_pk>/transcript/", views.transcript_upload, name="transcript-upload"),
    path("clusters/<int:cluster_pk>/rename/", views.cluster_rename, name="cluster-rename"),
    path("clusters/<int:cluster_pk>/vote/", views.vote, name="vote"),
    path("feedback/<int:item_pk>/move/", views.feedback_move, name="feedback-move"),
]
