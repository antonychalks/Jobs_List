from django.db import models
from django.contrib.auth.models import User
from multiselectfield import MultiSelectField
from autoslug import AutoSlugField

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
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    slug = models.SlugField(max_length=200, unique=True)
    medical = models.TextField(blank=True)
    emergency_name = models.CharField(max_length=50, blank=True)
    emergency_number = models.IntegerField(blank=True, default='0')
    certifications = models.TextField(blank=True)
    email = models.EmailField(blank=True)
    address = models.TextField(blank=True)
    postcode = models.CharField(blank=True)
    phone = models.IntegerField(blank=True, default='0')
    other_phone = models.IntegerField(blank=True, default='0')
    
    class Meta:
        ordering = ["role"]
    
    def __str__(self):
        return f"{self.user} | {self.role}"
    
    def get_trade_display(self):
        return ", ".join([dict(TRADES)[trade] for trade in self.trade])
    