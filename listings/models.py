from django.db import models



class listing(models.Model):
    """model representing a listing"""

    class listing_photo(models.Model):
        """model for the listing photos"""
        photo_id = models.BigAutoField(primary_key=True)
        photo_url = models.ImageField(upload_to='listing_images/', blank=True)


    status_choice = {
        ('available' , 'Available'),
        ('pending' , 'Pending'),
        ('sold' , 'Sold')

    }
    listing_id = models.BigAutoField(primary_key=True)
    street = models.CharField(max_length=250)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=2)
    zip = models.CharField(max_length=5)
    description = models.CharField(max_length=1000)
    property_price = models.DecimalField(max_digits=10, decimal_places=2)
    bedrooms = models.IntegerField()
    bathrooms = models.IntegerField
    sq_footage = models.IntegerField()
    status = models.CharField(max_length=10, choices = status_choice)
    created_date = models.DateField
    updated_date = models.DateField
    neighborhood = models.ForeignKey('neighborhood', on_delete=models.CASCADE)
    price= models.ForeignKey('price', on_delete=models.CASCADE)
    property_type = models.ForeignKey('property_type', on_delete=models.CASCADE)
    is_visible = models.BooleanField(default=True)
    is_featured = models.BooleanField(default=False)

    @property
    def full_address(self):
        """Returns the full addresss"""
        return f"{self.street} {self.city} {self.state} {self.zip}"

class neighborhood(models.Model):
    """model for a neighborhood type"""
    neighborhood_id = models.BigAutoField(primary_key = True)

class price(models.Model):
    """model for the price for the search report"""
    price_id = models.BigAutoField(primary_key = True)

class property_type(models.Model):
    """model for the property type"""
    property_type = models.BigAutoField(primary_key = True)
