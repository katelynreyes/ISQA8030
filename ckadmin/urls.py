from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('', views.dashboard, name='admin_dashboard'),

]