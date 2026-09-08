from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password

from .models import ActionItem, Cluster, Decision, FeedbackCycle, FeedbackItem, Project


class RegistrationForm(forms.ModelForm):
    display_name = forms.CharField(max_length=120)
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["username", "display_name", "password"]

    def clean_password(self):
        password = self.cleaned_data["password"]
        validate_password(password)
        return password

    def save(self, commit=True):
        user = User(username=self.cleaned_data["username"], first_name=self.cleaned_data["display_name"])
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ["name"]


class FeedbackCycleForm(forms.ModelForm):
    class Meta:
        model = FeedbackCycle
        fields = ["title"]


class FeedbackItemForm(forms.ModelForm):
    class Meta:
        model = FeedbackItem
        fields = ["category", "body", "is_anonymous"]
        widgets = {
            "body": forms.Textarea(attrs={"rows": 4}),
        }


class ClusterForm(forms.ModelForm):
    class Meta:
        model = Cluster
        fields = ["title"]


class DecisionForm(forms.ModelForm):
    class Meta:
        model = Decision
        fields = ["text"]
        widgets = {
            "text": forms.Textarea(attrs={"rows": 2}),
        }


class ActionItemForm(forms.ModelForm):
    class Meta:
        model = ActionItem
        fields = ["description", "owner", "due_date"]
        widgets = {
            "description": forms.Textarea(attrs={"rows": 2}),
            "due_date": forms.DateInput(attrs={"type": "date"}),
        }


class TranscriptForm(forms.Form):
    transcript = forms.CharField(widget=forms.Textarea(attrs={"rows": 8}))
