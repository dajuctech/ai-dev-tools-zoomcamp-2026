from django.contrib import admin

from .models import (
    ActionItem,
    Cluster,
    Decision,
    FeedbackCycle,
    FeedbackItem,
    Membership,
    Project,
    TranscriptProcessing,
    Vote,
)


admin.site.register(Project)
admin.site.register(Membership)
admin.site.register(FeedbackCycle)
admin.site.register(FeedbackItem)
admin.site.register(Cluster)
admin.site.register(Vote)
admin.site.register(Decision)
admin.site.register(ActionItem)
admin.site.register(TranscriptProcessing)
