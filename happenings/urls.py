from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="happenings"),
    path("<int:happening_id>/", views.details, name="details"),
]