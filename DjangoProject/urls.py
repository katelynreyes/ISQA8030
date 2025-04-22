from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static

from DjangoProject import settings

urlpatterns = [
    path("", include("home.urls")),
    path("home/", include("home.urls")),
    path("administration/", include("ckadmin.urls")),
    path("about/", include("contact.urls")),
    path("happenings/", include("happenings.urls")),
    path("listings/", include("listings.urls")),
    path("login/", include("login.urls")),
    path("admin/", admin.site.urls),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)