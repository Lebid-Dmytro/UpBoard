from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from main import settings

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("upboard_project.urls")),
    path("accounts/", include("django.contrib.auth.urls")),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
