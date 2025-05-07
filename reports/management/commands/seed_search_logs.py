from django.core.management.base import BaseCommand
from listings.models import SearchLog, property_type, neighborhood, price_search
from django.utils.timezone import now
import random

class Command(BaseCommand):
    help = 'Seeds the database with SearchLog entries for testing'

    def handle(self, *args, **kwargs):
        property_types = list(property_type.objects.all())
        neighborhoods = list(neighborhood.objects.all())
        price_ranges = list(price_search.objects.all())

        if not (property_types and neighborhoods and price_ranges):
            self.stdout.write(self.style.ERROR("Make sure property_type, neighborhood, and price_search have values."))
            return

        for _ in range(50):
            SearchLog.objects.create(
                property_type=random.choice(property_types),
                neighborhood=random.choice(neighborhoods),
                price_search=random.choice(price_ranges),
                timestamp=now()
            )

        self.stdout.write(self.style.SUCCESS("Successfully created 50 SearchLog entries"))
