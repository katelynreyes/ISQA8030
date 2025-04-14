from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("home/", include("home.urls")),
path("administration/", include("admin.urls")),
path("contact/", include("contact.urls")),
path("happenings/", include("happenings.urls")),
path("listings/", include("listings.urls")),
path("login/", include("login.urls")),
    path("admin/", admin.site.urls),
]