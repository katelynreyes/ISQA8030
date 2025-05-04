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
    def __str__(self):
        return f"{self.street}, {self.city})"


class listing_photo(models.Model):
    """model for the listing photos"""
    photo_id = models.BigAutoField(primary_key=True)
    photo_url = models.ImageField(upload_to='listing_images/', blank=True)
    listing = models.ForeignKey(listing, on_delete= models.CASCADE, null = 'True')
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.photo_url}"

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
    id = models.BigAutoField(primary_key=True)
    label = models.CharField(max_length=100, default="Unspecified")
    min_price = models.IntegerField(default=0)
    max_price = models.IntegerField(default=0)

    def __str__(self):
        return self.label


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