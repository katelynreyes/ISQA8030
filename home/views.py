from django.shortcuts import render
from .models import Listing

def index(request):
    listing = Listing.objects.first()  # show first for now
    return render(request, 'index.html', {
        'price': f"${listing.price:,.0f}",
        'property_type': listing.property_type,
        'neighborhood': listing.neighborhood
    }) if listing else render(request, 'index.html')
