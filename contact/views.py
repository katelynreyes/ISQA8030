from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("Contact app")
def contact_view(request):
    return render(request, 'contact/contact.html')