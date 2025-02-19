from django.contrib.auth.views import LoginView
from django.urls import path

from upboard_project.views import index, TaskListView, TaskCreateView, TaskDetailView, ClientReviewCreateView, \
    AddCommentView

urlpatterns = [
    path("", index, name="index"),
    path("login/", LoginView.as_view(), name="login"),
    path("tasks/<str:status>/", TaskListView.as_view(), name="filtered-task-list"),
    path("task/<int:pk>/", TaskDetailView.as_view(), name="task-detail"),
    path("task/<int:pk>/add-comment/", AddCommentView.as_view(), name="add-comment"),
    path("create/", TaskCreateView.as_view(), name="task-create", ),
    path("reviews/", ClientReviewCreateView.as_view(), name="client_review"),
]

app_name = "upboard_project"
