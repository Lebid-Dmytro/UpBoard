from datetime import timedelta

from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.timezone import now
from django.views import generic

from upboard_project.forms import TaskForm
from upboard_project.models import Task


def index(request):
    return render(request, "upboard_project/index.html")


class TaskListView(generic.ListView):
    model = Task
    template_name = "task_list.html"
    context_object_name = "tasks"

    def get_queryset(self):
        status = self.kwargs.get("status")
        if status == "done":
            return Task.objects.filter(status="done", closed_at__gte=now() - timedelta(days=30))
        elif status == "archive_done":
            return Task.objects.filter(status="done", closed_at__lt=now() - timedelta(days=30))
        elif status:
            return Task.objects.filter(status=status)
        return Task.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        status = self.kwargs.get("status")
        if status:
            context["status"] = status
        return context


class TaskDetailView(generic.DetailView):
    model = Task


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskForm
    template_name = "upboard_project/task_form.html"
    success_url = reverse_lazy("upboard_project:index")
