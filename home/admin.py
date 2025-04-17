from django.contrib import admin
from .models import Listing

admin.site.register(Listing)
from listings.models import listing, neighborhood, property_type, price

admin.site.register(listing)
admin.site.register(neighborhood)
admin.site.register(property_type)
admin.site.register(price)