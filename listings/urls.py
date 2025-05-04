from django.urls import path
from . import views
from .views import listings_list

urlpatterns = [
    path('', views.listings_list, name="listings"),
    path("<int:listing_id>/", views.details, name="details"),
    path('send-email/', views.send_test_email, name='send_test_email'),
    path('search/', views.search_listings, name='search-listings'),
    path('listings/', listings_list, name='listings'),


]
