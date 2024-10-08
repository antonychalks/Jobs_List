import uuid

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.text import slugify
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
    user = models.OneToOneField(
        User,
        related_name='user_profile',
        on_delete=models.CASCADE
    )
    role = models.IntegerField(choices=ROLE, default=0)
    trade = MultiSelectField(max_length=30, choices=TRADES)
    profile_image = CloudinaryField('image', default='placeholder', blank=True)
    fname = models.CharField('First name', max_length=50)
    lname = models.CharField('Last name', max_length=50)
    slug = models.SlugField(max_length=200, unique=True)
    medical = models.TextField('Medical Conditions', blank=True)
    certifications = models.TextField(blank=True)
    nok = models.CharField('Next of Kin', max_length=50, blank=True)
    nok_number = models.CharField(
        'Next of Kin contact number',
        blank=True,
        max_length=15
    )
    email = models.EmailField()
    street = models.CharField(blank=True, max_length=40)
    town_city = models.CharField('Town/City', blank=True, max_length=20)
    county = models.CharField(blank=True, max_length=25)
    postcode = models.CharField(blank=True, max_length=15)
    phone = models.CharField(max_length=15)
    other_phone = models.CharField(
        'Other Phone Number',
        blank=True,
        max_length=15)
    profile_complete = models.BooleanField(default=False)
    is_initial_signup = models.BooleanField(default=True)

    class Meta:
        ordering = ["role"]

    def get_role_display(self):
        """
        When called, displays the user-friendly role name
        rather than the integer.
        """
        dict_role = dict(ROLE)
        return dict_role.get(self.role)

    def get_trade_display(self):
        """ When called, displays the trade name rather than the code."""
        return ", ".join([dict(TRADES)[trade] for trade in self.trade])

    def generate_slug(self, user):
        """
        Generates the slug by appending a random string of numbers
        to the users' username
        """
        return slugify(user.username + "-" + str(uuid.uuid4()))

    def __str__(self):
        return (f"{self.user} | {self.get_role_display()} "
                f"| {self.get_trade_display()}")

    def save(self, *args, **kwargs):
        """ Rewrites the save function to generate the slug if there isn't one.
        Also checks if the profile is complete."""
        if (self.role and self.trade and self.fname and self.lname and
                self.nok and self.nok_number and self.email and
                self.street and self.town_city and self.postcode
                and self.phone):
            self.profile_complete = True
        else:
            self.profile_complete = False
        if not self.slug:
            self.generate_slug()
        super(UserProfile, self).save(*args, **kwargs)


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    Create or update the user profile
    """
    if created:
        slug = UserProfile().generate_slug(instance)
        user_profile = UserProfile.objects.create(user=instance, slug=slug)
    else:
        # Existing users: just save the profile
        slug = instance.user_profile.generate_slug(instance)
        instance.user_profile.slug = slug
        instance.user_profile.save()
