from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
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
    profile_image = CloudinaryField('image', default='placeholder', blank=True)
    fname = models.CharField('First name', max_length=50)
    lname = models.CharField('Last name', max_length=50)
    slug = models.SlugField(max_length=200, unique=True)
    medical = models.TextField('Medical Conditions', blank=True)
    nok = models.CharField('Next of Kin', max_length=50, blank=True)
    nok_number = models.CharField('Next of Kin contact number',blank=True, default='0', max_length=15)
    certifications = models.TextField(blank=True)
    email = models.EmailField(blank=True)
    street = models.CharField(blank=True , max_length=40)
    town_city = models.CharField('Town/City', blank=True, max_length=20)
    county = models.CharField(blank=True, max_length=25)
    postcode = models.CharField(blank=True, max_length=15)
    phone = models.CharField(blank=True, max_length=15)
    other_phone = models.CharField('Other Phone Number', blank=True, max_length=15)
    profile_complete = models.BooleanField(default=False)
    
    class Meta:
        ordering = ["role"]
        
    def get_trade_display(self):
        return ", ".join([dict(TRADES)[trade] for trade in self.trade])
    
    def __str__(self):
        return f"{self.user} | {self.get_role_display()} | {self.get_trade_display()}"

    def set_profile_complete(self):
        if self.role and self.trade and self.fname and self.lname and self.medical and self.nok and self.nok_number and self.certifications and self.email and self.street and self.town_city and self.postcode and self.phone:
            self.profile_complete = True
            self.save()


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    Create or update the user profile
    """
    if created:
        UserProfile.objects.create(user=instance)
    # Existing users: just save the profile
    instance.userprofile.save()

