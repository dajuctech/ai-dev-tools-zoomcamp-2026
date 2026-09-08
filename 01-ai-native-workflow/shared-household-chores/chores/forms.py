from django import forms

from .models import Chore, HouseholdMember


class HouseholdMemberForm(forms.ModelForm):
    class Meta:
        model = HouseholdMember
        fields = ["name"]
        widgets = {
            "name": forms.TextInput(attrs={"placeholder": "Name"}),
        }


class ChoreForm(forms.ModelForm):
    class Meta:
        model = Chore
        fields = ["title", "description", "assignee", "due_date"]
        widgets = {
            "title": forms.TextInput(attrs={"placeholder": "Chore title"}),
            "description": forms.Textarea(attrs={"rows": 4}),
            "due_date": forms.DateInput(attrs={"type": "date"}),
        }
