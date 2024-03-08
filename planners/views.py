from django.shortcuts import render, get_object_or_404, reverse
from django.forms import modelformset_factory
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from main.models import UserProfile as UserProfile
from tradesman.models import Job, Task
from .forms import UpdateContactDetailsForm, UpdateUserDetailsForm, NewUserForm, NewJobForm, EditJobForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def job_number():
    # Generate job number if it's not set yet
    job_number = 0
    # Retrieve the latest job number from the database
    latest_job = Job.objects.order_by('-job_number').first()
    if latest_job:
        job_number = latest_job.job_number + 1
    else:
        # If no jobs exist yet, start job numbers from 1
        job_number = 1

def planner_home(request):    
    if request.method == "POST":
        new_job_form = NewJobForm(data=request.POST)
        if new_job_form.is_valid():
            new_job = new_job_form.save(commit = False)
            new_job.created_by = request.user
            new_job.job_number = job_number()
            new_job.slug = new_job.job_number
            new_job.status = 0
            new_job.save()
            messages.success(request, 'Job Created!')
            return HttpResponseRedirect(reverse('planner_home'))
            
    
    job = Job.objects.all()
    newJob = NewJobForm()
    editJob = EditJobForm()
    
    return render(
        request,
        "planners/planner_home.html",
        {
            "job": job,
            "add_job_form": newJob,
            "edit_job_form": editJob
        }
    )
    
class UserList(generic.ListView):
    queryset = UserProfile.objects.all()
    context_object_name = 'UserList'
    template_name = "planners/list_tradesman.html"
    paginate_by = 6
    
def job_edit(request, job_id, slug):
    """
    Display an individual task for editing.
    """
    # Retrieve the job instance
    job = get_object_or_404(Job, slug=slug)
    
    if request.method == "POST":
        # Print out the request.POST dictionary to inspect the data
        print(request.POST)
        
        # Initialize form with task instance and data from request
        edit_job_form = NewJobForm(data=request.POST, instance=task)
        
        if edit_job_form.is_valid():
            # Save the form data to the task instance
            job.save()
            messages.success(request, 'Task Updated!')
            return HttpResponseRedirect(reverse('job_detail', args=[slug]))
        else:
            messages.error(request, 'Error updating task!')
    job = Job.objects.all()
    newJob = NewJobForm()
    editJob = EditJobForm()
    
    return render(
        request,
        "planners/planner_home.html",
        {
            "job": job,
            "add_job_form": newJob,
            "edit_job_form": editJob
        }
    )

@login_required
def user_detail(request, slug):
    queryset = UserProfile.objects.all()
    user = get_object_or_404(queryset, slug=slug)

    if request.method == "POST":
        if 'update_contact_details' in request.POST:
            update_contact_details_form = UpdateContactDetailsForm(request.POST, instance=user)
            if update_contact_details_form.is_valid():
                update_contact_details_form.save()
                messages.add_message(
                    request, messages.SUCCESS,
                    'Contact details updated successfully.'
                )
            else:
                messages.add_message(
                    request, messages.ERROR,
                    'Failed to update contact details. Please check the form.'
                )
            update_user_details_form = UpdateUserDetailsForm(instance=user)
        elif 'update_user_details' in request.POST:
            update_user_details_form = UpdateUserDetailsForm(request.POST, instance=user)
            if update_user_details_form.is_valid():
                update_user_details_form.save()
                messages.add_message(
                    request, messages.SUCCESS,
                    'User details updated successfully.'
                )
            else:
                messages.add_message(
                    request, messages.ERROR,
                    'Failed to update user details. Please check the form.'
                )
            update_contact_details_form = UpdateContactDetailsForm(instance=user)
    
    update_contact_details_form = UpdateContactDetailsForm(instance=user)
    update_user_details_form = UpdateUserDetailsForm(instance=user)

    return render(
        request,
        "planners/user_detail.html",
        {
            "user": user,
            "contact_form": update_contact_details_form,
            "user_details_form": update_user_details_form,
        },
    )

def add_user(request):
    if request.method == "POST":
        new_user_form = NewUserForm(data=request.POST)
        if new_user_form.is_valid():
            new_user_form.save()
            messages.success(request, 'New User Added!')
            return
    else:
        new_user_form = NewUserForm()

    return render(
        request,
        "planners/add_user.html",
        {
            "new_user_form": new_user_form,
        },
    )