from django.db import models
from django.contrib.auth.models import User
from multiselectfield import MultiSelectField
from cloudinary.models import CloudinaryField
from main.models import TRADES

# Create your models here.
class Job (models.Model):
    """
    Stores the profile of a user

    """
    slug = models.SlugField(max_length=200, unique=True)
    trades_required = MultiSelectField(max_length=30, choices=TRADES)
    job_number = models.IntegerField()
    phone = models.CharField(blank=True)
    other_phone = models.CharField('Other Phone Number', blank=True)
    email = models.EmailField(blank=True)
    street = models.CharField(blank=True)
    town_city = models.CharField('Town/City', blank=True)
    county = models.CharField(blank=True)
    postcode = models.CharField(blank=True)
    job_description = models.TextField()
    add_task = models.CharField()
    pending_task = models.CharField()
    
    def get_trade_display(self):
        return ", ".join([dict(TRADES)[trade] for trade in self.trade])