from random import choices

from django.db import models



class listing(models.Model):
    """model representing a listing"""

    status_choice = [
        ('Available' , 'Available'),
        ('Pending' , 'Pending'),
        ('Sold' , 'Sold')

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
    listing = models.ForeignKey(listing, on_delete= models.CASCADE, null = 'True')


class neighborhood(models.Model):
    """model for a neighborhood type"""
    name = [
        ('Aksarben Village','Aksarben Village'),
        ('Benson','Benson'),
        ('Blackstone', 'Blackstone'),
        ('Downtown', 'Downtown'),
        ('Dundee', 'Dundee'),
        ('Elkhorn', 'Elkhorn'),
        ('Field Club', 'Field Club'),
        ('Midtown Crossing', 'Midtown Crossing'),
        ('Millard', 'Millard'),
        ('Old Market', 'Old Market'),
        ('Regency', 'Regency'),
        ('South Omaha', 'South Omaha'),
        ('West Omaha', 'West Omaha')
    ]
    neighborhood_id = models.BigAutoField(primary_key=True)
    neighborhood_name = models.CharField(max_length=100, choices=name)

    def __str__(self):
        return self.neighborhood_name


class price_search(models.Model):
    """model for the price for the search report"""
    price_choice = {
        ('50,001 - 100,000', '50,001 - 100,000'),
        ('100,001 - 150,000', '100,001 - 150,000'),
        ('150,001 - 200,000', '150,001 - 200,000'),
        ('200,001 - 250,000', '200,001 - 250,000'),
        ('250,001 - 300,000', '250,001 - 300,000'),
        ('3000,01 - 350,000', '300,001 - 350,000'),
        ('350,001 - 400,000', '350,001 - 400,000'),
        ('400,001 - 450,000', '400,001 - 450,000'),
        ('450,001 - 500,000', '450,001 - 500,000'),
        ('500,001 - 550,000', '500,001 - 550,000'),
        ('550,001 - 600,000', '550,001 - 600,000'),
        ('600,001 - 650,000', '600,001 - 650,000'),
        ('650,001 - 700,000', '650,001 - 700,000'),
        ('700,001 - 750,000', '700,001 - 750,000'),
        ('750,001 - 800,000', '750,001 - 800,000'),
        ('800,001 - 850,000', '800,001 - 850,000'),
        ('850,001 - 900,000', '850,001 - 900,000'),
        ('900,001 - 950,000', '900,001 - 950,000'),
        ('950,001 - 1,000,000', '950,001 - 1,000,000')

    }
    price_id = models.BigAutoField(primary_key=True)
    price_range = models.CharField(max_length=100, choices=price_choice)

    def __str__(self):
        return self.price_range

class property_type(models.Model):
    """model for the property type"""
    types = [
        ('Bungalow', 'Bungalow'),
        ('Colonial', 'Colonial'),
        ('Condominium', 'Condominium'),
        ('Craftsman', 'Craftsman'),
        ('Log Cabin', 'Log Cabin'),
        ('Modern', 'Modern'),
        ('Ranch', 'Ranch'),
        ('Split Level', 'Split Level'),
        ('Townhome', 'Townhome'),
        ('Tudor', 'Tudor'),
        ('Victorian', 'Victorian')
    ]
    property_id = models.BigAutoField(primary_key=True)
    property_type = models.CharField(max_length=100, choices=types)

    def __str__(self):
        return self.property_type

class SearchLog(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    property_type = models.ForeignKey('property_type', on_delete=models.SET_NULL, null=True, blank=True)
    neighborhood = models.ForeignKey('neighborhood', on_delete=models.SET_NULL, null=True, blank=True)
    price_search = models.ForeignKey('price_search', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"Search at {self.timestamp.strftime('%Y-%m-%d %H:%M')}"