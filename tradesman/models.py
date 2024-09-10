from django.db import models
from django.contrib.auth.models import User
from django.template import RequestContext
from django.template.context_processors import request
from multiselectfield import MultiSelectField
from cloudinary.models import CloudinaryField
from main.models import UserProfile, TRADES

JOB_STATUS = ((0, "Unassigned"), (1, "Pending Start"), (2, "In Progress"), (3, "Completed"), (4, "No Tasks"))

PLANNERS = UserProfile.role
# Create your models here.


class Job(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=200, unique=True)
    job_number = models.IntegerField()
    customer_name = models.CharField(max_length=30)
    phone = models.CharField(max_length=15)
    other_phone = models.CharField('Other Phone Number', blank=True, max_length=15)
    email = models.EmailField()
    street = models.CharField(max_length=40)
    town_city = models.CharField('Town/City', blank=True, max_length=20)
    county = models.CharField(blank=True, max_length=25)
    postcode = models.CharField(max_length=10)
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

    def set_job_status(self):
        if self.Tasks.all().count() == 0:
            self.status = 4
        else:
            task_count = 0
            task_complete_count = 0
            for task in self.Tasks.all:
                task_count += 1
                if task.is_completed:
                    task_complete_count += 1
            if task_complete_count == task_count:
                self.status = 3
            elif task_complete_count >= 1:
                self.status = 2
            else:
                for task in self.Tasks.all:
                    if task.tradesman_assigned:
                        self.status = 1
    
    def get_status_display(self):
        return dict(JOB_STATUS)[self.status]

    @property
    def is_assigned_to_current_user(self):
        user = User.objects.get(username=RequestContext(request)['user'])
        return any(task.tradesman_assigned.filter(user=user).exists()
                   for task in self.Tasks.all())


class Task(models.Model):
    """
    Stores the tasks for each job
    """
    job = models.ForeignKey(Job, on_delete=models.CASCADE,
                             related_name="Tasks" )
    description = models.CharField(max_length=255)
    trades_required = MultiSelectField(max_length=30, choices=TRADES, blank=True)
    tradesman_assigned = models.ManyToManyField("main.UserProfile", related_name="tradesman", blank=True)
    time_required = models.CharField(blank=True, max_length=25)
    is_completed = models.BooleanField(default=False)
    
    class Meta:
        ordering = ["is_completed"]

    def tradesman_assigned_boolean(self):
        tradesman_count = 0
        for tradesman in self.tradesman_assigned.all():
            tradesman_count += 1

        if tradesman_count == 0:
            return False
        else:
            return True
