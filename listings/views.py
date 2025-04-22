from django.http import HttpResponse
from django.views import generic
from listings.models import listing
from django.shortcuts import get_object_or_404, render

# def index(request):
#     return HttpResponse("Listings app")

def listings_list(request):
    listings = listing.objects.all()  # call with () to get data
    return render(request, 'listings/listings.html', {'listings': listings})


def details(request, listing_id):
    listingItem = get_object_or_404(listing, pk=listing_id)
    return render(request, "listings/details.html", {"listingItem": listingItem})