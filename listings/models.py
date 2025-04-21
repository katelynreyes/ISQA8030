from random import choices

from django.db import models



class listing(models.Model):
    """model representing a listing"""

    status_choice = [
        ('available' , 'Available'),
        ('pending' , 'Pending'),
        ('sold' , 'Sold')

]
    listing_id = models.BigAutoField(primary_key=True)
    street = models.CharField(max_length=250)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=2)
    zip = models.CharField(max_length=5)
    description = models.CharField(max_length=1000)
    property_price = models.DecimalField(max_digits=10, decimal_places=2)
    bedrooms = models.IntegerField()
    bathrooms = models.IntegerField()
    sq_footage = models.IntegerField()
    status = models.CharField(max_length=10, choices = status_choice)
    created_date = models.DateField()
    updated_date = models.DateField()
    neighborhood = models.ForeignKey('neighborhood', on_delete=models.CASCADE)
    price_search= models.ForeignKey('price_search', on_delete=models.CASCADE)
    property_type = models.ForeignKey('property_type', on_delete=models.CASCADE)
    is_visible = models.BooleanField(default=True)
    is_featured = models.BooleanField(default=False)

    @property
    def full_address(self):
        """Returns the full address"""
        return f"{self.street} {self.city} {self.state} {self.zip}"


class listing_photo(models.Model):
    """model for the listing photos"""
    photo_id = models.BigAutoField(primary_key=True)
    photo_url = models.ImageField(upload_to='listing_images/', blank=True)
    listing = models.ForeignKey('listing', on_delete= models.CASCADE, null=True)


class neighborhood(models.Model):
    """model for a neighborhood type"""
    name = [
        ('Aksarben Village','aksarben village'),
        ('Benson','benson'),
        ('Blackstone', 'blackstone'),
        ('Downtown', 'downtown'),
        ('Dundee', 'dundee'),
        ('Elkhorn', 'elkhorn'),
        ('Field Club', 'field club'),
        ('Midtown Crossing', 'midtown crossing'),
        ('Millard', 'millard'),
        ('Old Market', 'old market'),
        ('Regency', 'regency'),
        ('South Omaha', 'south omaha'),
        ('West Omaha', 'west omaha')
    ]
    neighborhood_id = models.BigAutoField(primary_key=True)
    neighborhood_name = models.CharField(max_length=100, choices=name)


class price_search(models.Model):
    """model for the price for the search report"""
    price_choice = {
        ('50001 - 100000', '50001 - 100000'),
        ('100001 - 150000', '100001 - 150000'),
        ('150001 - 200000', '150001 - 200000'),
        ('200001 - 250000', '200001 - 250000'),
        ('250001 - 300000', '250001 - 300000'),
        ('300001 - 350000', '300001 - 350000'),
        ('350001 - 400000', '350001 - 400000'),
        ('400001 - 450000', '400001 - 450000'),
        ('450001 - 500000', '450001 - 500000'),
        ('500001 - 550000', '500001 - 550000'),
        ('550001 - 600000', '550001 - 600000'),
        ('600001 - 650000', '600001 - 650000'),
        ('650001 - 700000', '650001 - 700000'),
        ('700001 - 750000', '700001 - 750000'),
        ('750001 - 800000', '750001 - 800000'),
        ('800001 - 850000', '800001 - 850000'),
        ('850001 - 900000', '850001 - 900000'),
        ('900001 - 950000', '900001 - 950000'),
        ('950001 - 1000000', '950001 - 1000000')

    }
    price_id = models.BigAutoField(primary_key=True)
    price_range = models.CharField(max_length=100, choices=price_choice)


class property_type(models.Model):
    """model for the property type"""
    types = [
        ('Bungalow', 'bungalow'),
        ('Colonial', 'colonial'),
        ('Condominium', 'condominium'),
        ('Craftsman', 'craftsman'),
        ('Log Cabin', 'log cabin'),
        ('Modern', 'modern'),
        ('Ranch', 'ranch'),
        ('Split Level', 'split level'),
        ('Townhome', 'townhome'),
        ('Tudor', 'tudor'),
        ('Victorian', 'victorian')
    ]
    property_id = models.BigAutoField(primary_key=True)
    property_type = models.CharField(max_length=100, choices=types)


