from django.urls import path
from . import views

urlpatterns = [
    path('', views.about, name='about'),
    path('send-email/', views.send_test_email, name='send_test_email'),

]