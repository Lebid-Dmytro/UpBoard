from datetime import timedelta

from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.core.checks import messages
from django.db.models import Count
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.utils.timezone import now
from django.views import generic, View
from django.views.generic import UpdateView

from upboard_project.forms import TaskForm, ClientReviewForm
from upboard_project.models import Task, ClientReview, Worker, Comment


def index(request):
    return render(request, "upboard_project/index.html")


class TaskListView(LoginRequiredMixin, generic.ListView):
    model = Task
    template_name = "task_list.html"
    context_object_name = "tasks"

    def get_queryset(self):
        status = self.kwargs.get("status")
        queryset = Task.objects.filter(company=self.request.user.company)

        if status == "done":
            queryset = queryset.filter(status="done", closed_at__gte=now() - timedelta(days=30))
        elif status == "archive_done":
            queryset = queryset.filter(status="done", closed_at__lt=now() - timedelta(days=30))
        elif status:
            queryset = queryset.filter(status=status)

        return queryset.annotate(num_comments=Count("comments"))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        status = self.kwargs.get("status")
        if status:
            context["status"] = status
        return context


class TaskDetailView(generic.DetailView):
    model = Task
    template_name = "upboard_project/task_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["comments"] = self.object.comments.select_related("worker").all()
        return context


class AddCommentView(LoginRequiredMixin, View):
    def post(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        worker = Worker.objects.get(pk=request.user.pk)
        text = request.POST.get("text")
        parent_id = request.POST.get("parent_id")

        parent_comment = None
        if parent_id:
            parent_comment = get_object_or_404(Comment, pk=parent_id)

        if text:
            Comment.objects.create(task=task, worker=worker, text=text, parent=parent_comment)

        return redirect(reverse("upboard_project:task-detail", kwargs={"pk": task.pk}))


class TaskCreateView(LoginRequiredMixin, generic.CreateView):
    model = Task
    form_class = TaskForm
    template_name = "upboard_project/task_form.html"
    success_url = reverse_lazy("upboard_project:index")

    def form_valid(self, form):
        task = form.save(commit=False)
        task.company = self.request.user.company
        task.save()
        task.assignees.add(self.request.user)
        return super().form_valid(form)


class ClientReviewCreateView(generic.CreateView):
    model = ClientReview
    form_class = ClientReviewForm
    template_name = "upboard_project/reviews_form.html"
    success_url = reverse_lazy("upboard_project:index")


class CustomLoginView(LoginView):
    def form_valid(self, form):
        user = form.get_user()
        login(self.request, user)

        if user.company:
            return redirect("task-list")
        return redirect("no-company")


class TaskStatusUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    fields = ["status"]
    template_name = "task_detail.html"
    success_url = reverse_lazy("upboard_project:task-detail")

    def form_valid(self, form):
        form.save()
        return redirect("upboard_project:task-detail", pk=self.object.pk)
