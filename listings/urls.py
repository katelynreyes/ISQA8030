from django.urls import path

from . import views

urlpatterns = [
    path('', views.listings_list, name="listing"),
]
