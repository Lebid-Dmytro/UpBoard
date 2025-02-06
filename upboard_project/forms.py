from django import forms
from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = [
            "name",
            "description",
            "task_type",
            "assignees",
            "status",
        ]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "description": forms.Textarea(attrs={"class": "form-control"}),
            "task_type": forms.Select(attrs={"class": "form-control"}),
            "assignees": forms.SelectMultiple(attrs={"class": "form-control"}),
            "status": forms.Select(attrs={"class": "form-control"}),
        }
