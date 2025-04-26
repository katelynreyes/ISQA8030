from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test


def index(request):
    return HttpResponse("Admin app")

@user_passes_test(lambda u: u.is_superuser)
def dashboard(request):
    return render(request, 'ckadmin/dashboard.html')