from django.db import models
from django.contrib.auth.models import User
from multiselectfield import MultiSelectField
from phonenumber_field.modelfields import PhoneNumberField

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
    emergency_number = models.CharField(blank=True, default='0')
    certifications = models.TextField(blank=True)
    email = models.EmailField(blank=True)
    address_ln_1 = models.CharField(blank=True)
    address_ln_2 = models.CharField(blank=True)
    address_ln_3 = models.CharField(blank=True)
    postcode = models.CharField(blank=True)
    phone = models.CharField(blank=True)
    other_phone = models.CharField(blank=True)
    
    class Meta:
        ordering = ["role"]
    
    def __str__(self):
        return f"{self.user} | {self.role}"
    
    def get_trade_display(self):
        return ", ".join([dict(TRADES)[trade] for trade in self.trade])
    