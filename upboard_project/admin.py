from django.contrib import admin
from upboard_project.models import TypeTask, Position, Task, Worker


class WorkerAdmin(admin.ModelAdmin):
    list_display = (
        "username", "email", "first_name", "last_name", "get_positions"
    )

    search_fields = ("username", "email", "first_name", "last_name")

    def get_positions(self, obj):
        return ", ".join([position.name for position in obj.position.all()])

    get_positions.short_description = "Positions"

    fields = (
        "username", "email", "password", "first_name", "last_name", "position"
    )

    list_filter = ("position",)


admin.site.register(Worker, WorkerAdmin)
admin.site.register(TypeTask)
admin.site.register(Position)


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("name", "status", "opened_at", "closed_at")
    list_filter = ("status", "opened_at", "closed_at")
    search_fields = ("name", "description")
