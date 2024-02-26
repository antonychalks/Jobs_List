from django.db import models
from django.contrib.auth.models import User
from multiselectfield import MultiSelectField
from cloudinary.models import CloudinaryField

ROLE = ((0, "Planner"), (1, "Tradesman"))

TRADES = [
    ("Ca", "Carpenter"),
    ("Pl", "Plumber"),
    ("El", "Electrician"),
    ("Pa", "Plasterer"),
    ("Gw", "Groundsworker"),
    ("De", "Decorator"),
    ("Ga", "Gas"),
    ("AD", "Planner")
    ]


# Create your models here.

class UserProfile (models.Model):
    """
    Stores the profile of a user

    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.IntegerField(choices=ROLE, default=0)
    trade = MultiSelectField(max_length=30, choices=TRADES)
    profile_image = CloudinaryField('image', default='placeholder')
    fname = models.CharField('First name', max_length=50)
    lname = models.CharField('Last name', max_length=50)
    slug = models.SlugField(max_length=200, unique=True)
    medical = models.TextField('Medical Conditions', blank=True)
    nok = models.CharField('Next of Kin', max_length=50, blank=True)
    nok_number = models.CharField('Next of Kin contact number',blank=True, default='0')
    certifications = models.TextField(blank=True)
    email = models.EmailField(blank=True)
    street = models.CharField(blank=True)
    town_city = models.CharField('Town/City', blank=True)
    county = models.CharField(blank=True)
    postcode = models.CharField(blank=True)
    phone = models.CharField(blank=True)
    other_phone = models.CharField('Other Phone Number', blank=True)
    
    class Meta:
        ordering = ["role"]
    
    def __str__(self):
        return f"{self.user} | {self.role}"
    
    def get_trade_display(self):
        return ", ".join([dict(TRADES)[trade] for trade in self.trade])
    