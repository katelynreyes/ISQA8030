from django.http import HttpResponse
from django.views import generic
from listings.models import listing
from django.shortcuts import get_object_or_404, render
from django.contrib.humanize.templatetags.humanize import intcomma

# def index(request):
#     return HttpResponse("Listings app")

def listings_list(request):
    listings = listing.objects.all()
    for listing_item in listings:
        # Get the first photo for each listing
        listing_item.first_photo = listing_item.listing_photo_set.first()
    return render(request, 'listings/listings.html', {'listings': listings})


def details(request, listing_id):
    listingItem = get_object_or_404(listing, pk=listing_id)
    return render(request, "listings/details.html", {"listingItem": listingItem})





