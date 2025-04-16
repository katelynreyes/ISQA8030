
from django.db import models

class Listing(models.Model):
    title = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    property_type = models.CharField(max_length=50)
    neighborhood = models.CharField(max_length=100)
    image = models.ImageField(upload_to='listing_images/', blank=True)

    def __str__(self):
        return self.title
