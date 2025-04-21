from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from listings.models import listing

def index(request):
    return HttpResponse("Listings app")

def details(request, listing_id):
    listingItem = get_object_or_404(listing, pk=listing_id)
    return render(request, "listings/details.html", {"listingItem": listingItem})