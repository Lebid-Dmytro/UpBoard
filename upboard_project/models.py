from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.exceptions import ValidationError
from django.utils.timezone import now


class TypeTask(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Position(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Worker(AbstractUser):
    position = models.ManyToManyField(Position, related_name="workers")

    groups = models.ManyToManyField(
        "auth.Group",
        related_name="workers_groups",
        blank=True,
        help_text="The groups this user belongs to."
    )

    user_permissions = models.ManyToManyField(
        "auth.Permission",
        related_name="workers_permissions",
        blank=True,
        help_text="Specific permissions for this user."
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.username})"


class Task(models.Model):
    STATUS_CHOICES = [
        ("to_do", "To Do"),
        ("in_progress", "In Progress"),
        ("done", "Done"),
    ]

    name = models.CharField(max_length=255)
    description = models.TextField()
    task_type = models.ForeignKey(
        "TypeTask", on_delete=models.SET_NULL, null=True, related_name="tasks"
    )
    assignees = models.ManyToManyField("Worker", related_name="tasks")
    status = models.CharField(
        max_length=50, choices=STATUS_CHOICES, default="to_do"
    )
    opened_at = models.DateTimeField(auto_now_add=True)
    closed_at = models.DateTimeField(null=True, blank=True)

    def save(self, *args, **kwargs):
        self.clean()

        if self.status == "done" and not self.closed_at:
            self.closed_at = now()
        elif self.status != "done" and self.closed_at:
            self.closed_at = None

        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class ClientReview(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    review = models.TextField()
    photo = models.ImageField(upload_to="review_photos/", blank=True, null=True)

    def __str__(self):
        return self.review[:50]
