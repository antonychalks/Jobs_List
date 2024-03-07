from django.db import models
from django.contrib.auth.models import User
from multiselectfield import MultiSelectField
from cloudinary.models import CloudinaryField
from main.models import UserProfile, TRADES

JOB_STATUS = ((0, "Unassigned"), (1, "Pending Start"), (2, "In progress"), (3, "Completed"))

PLANNERS = UserProfile.role
# Create your models here.


class Job(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=200, unique=True)
    job_number = models.IntegerField()
    customer_name = models.CharField(max_length=30)
    phone = models.CharField(blank=True)
    other_phone = models.CharField('Other Phone Number', blank=True)
    email = models.EmailField(blank=True)
    street = models.CharField(blank=True)
    town_city = models.CharField('Town/City', blank=True)
    county = models.CharField(blank=True)
    postcode = models.CharField(blank=True)
    job_description = models.TextField(blank=True)
    status = models.IntegerField('Job Status', choices=JOB_STATUS)

    def save(self, *args, **kwargs):
        # Generate job number if it's not set yet
        if not self.job_number:
            # Retrieve the latest job number from the database
            latest_job = Job.objects.order_by('-job_number').first()
            if latest_job:
                self.job_number = latest_job.job_number + 1
            else:
                # If no jobs exist yet, start job numbers from 1
                self.job_number = 1
        if not self.slug:
            self.slug = self.job_number

        super(Job, self).save(*args, **kwargs)
    
    def get_status_display(self):
        return dict(JOB_STATUS)[self.status]

class Task(models.Model):
    """
    Stores the tasks for each job
    """
    job = models.ForeignKey(Job, on_delete=models.CASCADE,
                             related_name="Tasks" )
    description = models.CharField(max_length=255)
    trades_required = MultiSelectField(max_length=30, choices=TRADES, blank=True)
    tradesman_assigned = models.ManyToManyField("main.UserProfile", blank=True)
    time_required = models.CharField(blank=True)
    is_completed = models.BooleanField(default=False)
    
    class Meta:
        ordering = ["is_completed"]