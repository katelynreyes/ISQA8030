from django.shortcuts import render
from listings.models import listing, listing_photo

def index(request):
    featured_listings = listing.objects.filter(is_visible=True, is_featured=True)
    listing_to_show = None
    listing_photo_url = None

    if featured_listings.exists():
        if featured_listings.count() == 1:
            listing_to_show = featured_listings.first()
        else:
            available_featured = featured_listings.filter(status='available')
            if available_featured.count() == 1:
                listing_to_show = available_featured.first()

    if listing_to_show:
        first_photo = listing_photo.objects.filter(listing=listing_to_show).first()
        if first_photo and first_photo.photo_url:
            listing_photo_url = first_photo.photo_url.url  # important: .url, not just .photo_url

    context = {
        'listing': listing_to_show,
        'listing_photo_url': listing_photo_url,
    } if listing_to_show else {}

    return render(request, 'home/index.html', context)