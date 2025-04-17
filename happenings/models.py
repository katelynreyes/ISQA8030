from django.db import models

from DjangoProject import settings


class Happening(models.Model):
    class HappeningCategory(models.TextChoices):
        OMAHA_AREA_EVENT = 'Omaha Area Event', 'Omaha Area Event'
        PLACE_TO_VISIT = 'Place to Visit', 'Place to Visit'
        FAMILY_ACTIVITY = 'Family Activity', 'Family Activity'
        GREAT_PLACE_TO_EAT = 'Great Place to Eat', 'Great Place to Eat'

    happening_id = models.AutoField(primary_key=True)
    category = models.CharField(
        max_length=100,
        choices=HappeningCategory.choices,
        default=HappeningCategory.OMAHA_AREA_EVENT,
    )
    happening_description = models.TextField()
    photo = models.ImageField(upload_to='happenings/')
    url = models.TextField()
    happening_created_date = models.DateTimeField(auto_now_add=True)