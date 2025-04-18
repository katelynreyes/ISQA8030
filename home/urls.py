from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('listings/', views.listings, name='listings'),
    path('happenings/', views.happenings, name='happenings'),
]
