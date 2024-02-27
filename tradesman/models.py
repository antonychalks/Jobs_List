from django.db import models
from django.contrib.auth.models import User
from multiselectfield import MultiSelectField
from cloudinary.models import CloudinaryField
from main.models import UserProfile, TRADES

JOB_STATUS = ((0, "Unassigned"), (1, "Pending Start"), (2, "In progress"), (3, "Completed"))

# Create your models here.

class Job (models.Model):
    """
    Stores the details of a job

    """
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=200, unique=True)
    trades_required = MultiSelectField(max_length=30, choices=TRADES)
    tradesman_assigned = models.ManyToManyField("main.UserProfile")
    job_number = models.IntegerField()
    phone = models.CharField(blank=True)
    other_phone = models.CharField('Other Phone Number', blank=True)
    email = models.EmailField(blank=True)
    street = models.CharField(blank=True)
    town_city = models.CharField('Town/City', blank=True)
    county = models.CharField(blank=True)
    postcode = models.CharField(blank=True)
    job_description = models.TextField()
    status = models.IntegerField('Job Status', choices=JOB_STATUS)

    
    def __str__(self):
        return self.title
    
    def get_status_display(self):
        return ", ".join([dict(TRADES)[trade] for trade in self.trade])

class Task(models.Model):
    """
    Stores the tasks for each job
    """
    description = models.CharField(max_length=255)
    is_completed = models.BooleanField(default=False)
    
    def __str__(self):
        return self.description
    
class JobTask(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    is_completed = models.BooleanField(default=False)  # Represents completion status of task for this job

    def __str__(self):
        return f"{self.job} - {self.task}"