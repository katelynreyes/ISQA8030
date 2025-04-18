from django.urls import path, include
from django.contrib import admin
urlpatterns = [
    path('', include('home.urls')),
    path('contact/', include('contact.urls')),
    path('happenings/', include('happenings.urls')),
    path('listings/', include('listings.urls')),
    path('login/', include('login.urls')),
    path('admin/', include('admin.urls')),
    path('admin/', admin.site.urls),
]
