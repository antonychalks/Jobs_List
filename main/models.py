from django.db import models
from django.contrib.auth.models import User
from multiselectfield import MultiSelectField

ROLE = ((0, "Planner"), (1, "Tradesman"))
TRADES = [
    ("Ca", "Carpenter"),
    ("Pl", "Plumber"),
    ("El", "Electrician"),
    ("Pa", "Plasterer"),
    ("Gw", "Groundsworker"),
    ("De", "Decorator"),
    ("Ga", "Gas"),
    ]

# Create your models here.

class UserProfile (models.Model):
    """
    Stores the profile of a user
    Args:
        models (_type_): _description_
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.IntegerField(choices=ROLE, default=1)
    trade = MultiSelectField(max_length=2, choices=TRADES)
    