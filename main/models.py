from django.db import models
from django.contrib.auth.models import User
from multiselectfield import MultiSelectField
from autoslug import AutoSlugField

Planner = 0
Tradesman = 1

ROLE = ((Planner, "Planner"), (Tradesman, "Tradesman"))
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
    
    class Meta:
        ordering = ["role"]
    
    def __str__(self):
        return f"{self.user} | {self.role}"
    