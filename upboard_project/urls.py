from django.urls import path

from upboard_project.views import index, TaskListView, TaskCreateView, TaskDetailView

urlpatterns = [
    path("", index, name="index"),
    # path(
    #     "tasks/",
    #     TaskListView.as_view(),
    #     name="task-list",
    # ),
    path("tasks/<str:status>/", TaskListView.as_view(), name="filtered-task-list"),
    path(
        "detail/<int:pk>/",
        TaskDetailView.as_view(),
        name="task-detail",
    ),
    path(
        "create/",
        TaskCreateView.as_view(),
        name="task-create",
    ),
]

app_name = "upboard_project"
