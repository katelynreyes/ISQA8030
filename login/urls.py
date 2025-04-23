from django.urls import path
from django.contrib.auth import views as auth_views

class LogoutViaGet(auth_views.LogoutView):
    http_method_names = [ 'get', 'post' ]

urlpatterns = [
    path('', auth_views.LoginView.as_view(template_name='login/login.html', next_page='/admin/'), name='login'),
]
