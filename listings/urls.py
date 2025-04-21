from django.urls import path

from . import views

urlpatterns = [
    path('', views.listings_list, name="listing"),
    path("<int:listing_id>/", views.details, name="details"),
]
