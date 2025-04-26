from django.shortcuts import render
from .models import Listing

def index(request):
    listing = Listing.objects.first()
    context = {'listing': listing} if listing else {}
    return render(request, 'home/index.html', context)
