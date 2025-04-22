from django.urls import path

from . import views

urlpatterns = [
    path('', views.listings_list, name="listings"),
    path("<int:listing_id>/", views.details, name="details"),
]
