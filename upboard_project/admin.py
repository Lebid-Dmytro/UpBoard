from django.contrib import admin
from django.contrib.auth.hashers import make_password

from upboard_project.models import TypeTask, Position, Task, Worker, Company


class WorkerAdmin(admin.ModelAdmin):
    list_display = (
        "username",
        "email",
        "first_name",
        "last_name",
        "get_positions",
        "company"
    )
    search_fields = ("username", "email", "first_name", "last_name")
    list_filter = ("position",)

    def get_positions(self, obj):
        return ", ".join([position.name for position in obj.position.all()])

    get_positions.short_description = "Positions"

    fields = (
        "username", "email", "password", "first_name", "last_name", "company"
    )
    filter_horizontal = ("position",)

    def save_model(self, request, obj, form, change):
        if form.cleaned_data.get("password"):
            obj.password = make_password(form.cleaned_data["password"])
        super().save_model(request, obj, form, change)


admin.site.register(Worker, WorkerAdmin)
admin.site.register(TypeTask)
admin.site.register(Position)
admin.site.register(Company)


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("name", "status", "opened_at", "closed_at")
    list_filter = ("status", "opened_at", "closed_at")
    search_fields = ("name", "description")
