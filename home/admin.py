from django.contrib import admin
from listings.models import listing, neighborhood, property_type, listing_photo, price_search

class photo_inline(admin.TabularInline):
    model = listing_photo
    extra = 0
    fields = ["photo_url", "order"]
    ordering = ['order']

class listing_admin(admin.ModelAdmin):
    inlines = [photo_inline

    ]


admin.site.register(listing, listing_admin)
admin.site.register(neighborhood)
admin.site.register(property_type)
admin.site.register(price_search)
admin.site.register(listing_photo)

