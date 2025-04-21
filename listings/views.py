from django.http import HttpResponse
from django.views import generic
from listings.models import listing
from django.shortcuts import render

# def index(request):
#     return HttpResponse("Listings app")

def listings_list(request):
    listings = listing.objects.all()  # call with () to get data
    return render(request, 'listings.html', {'listings': listings})
