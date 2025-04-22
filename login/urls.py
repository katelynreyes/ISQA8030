from django.urls import path
from django.contrib.auth import views as auth_views

class CustomLogoutView(auth_views.LogoutView):
    http_method_names = [ 'get', 'post' ]

urlpatterns = [
    path('', auth_views.LoginView.as_view(template_name='login/login.html', next_page='/admin/'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
]
