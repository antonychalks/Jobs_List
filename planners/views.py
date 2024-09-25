from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from main.models import UserProfile as UserProfile
from tradesman.models import Job
from .forms import (
    UpdateContactDetailsForm,
    UpdateUserDetailsForm,
    NewUserForm, NewJobForm,
    EditJobForm
)
from django.contrib.auth.decorators import login_required


# Create your views here.
def job_number():
    """
    Generates a random job number
    if the job doesn't have a number.
    """
    # Retrieve the latest job number from the database
    latest_job = Job.objects.order_by('-job_number').first()
    if latest_job:
        job_num = latest_job.job_number + 1
    else:
        # If no jobs exist yet, start job numbers from 1
        job_num = 1
    return job_num


def planner_home(request):
    """
    Renders the planner home page and deals
    with POST requests from the NewJobForm
    """
    if request.method == "POST":
        new_job_form = NewJobForm(data=request.POST)
        # If the form is valid, the created_by, job_number,
        # slug and status all get added to the instance.
        if new_job_form.is_valid():
            new_job = new_job_form.save(commit=False)
            new_job.created_by = request.user
            new_job.job_number = job_number()
            new_job.slug = new_job.job_number
            new_job.status = 0
            new_job.save()
            messages.success(request, 'Job Created!')
            return HttpResponseRedirect(reverse('planner_home'))

    job = Job.objects.all()
    new_job = NewJobForm()
    edit_job = EditJobForm()
    user_profile = UserProfile.objects.get(user=request.user)

    return render(
        request,
        "planners/planner_home.html",
        {
            "user_profile": user_profile,
            "job": job,
            "add_job_form": new_job,
            "edit_job_form": edit_job
        }
    )


class UserList(generic.ListView):
    """ Renders the user list page """
    queryset = UserProfile.objects.all()
    context_object_name = 'UserList'
    template_name = "planners/list_user.html"
    paginate_by = 6


def job_edit(request, job_id, slug):
    """
    Handles the POST requests from the edit job form.
    """
    # Retrieve the job instance
    job = get_object_or_404(Job, pk=job_id, slug=slug)

    if request.method == "POST":
        # Initialize form with task instance and data from request
        edit_job_form = EditJobForm(data=request.POST, instance=job)
        # Saves the instance of the Job and works out the job status.
        if edit_job_form.is_valid():
            # Save the form data to the task instance
            job = edit_job_form.save(commit=False)
            job.save()
            messages.success(request, 'Task Updated!')
            return HttpResponseRedirect(reverse('planner_home'))
        else:
            messages.error(request, 'Error updating task!')

    new_job = NewJobForm()
    edit_job = EditJobForm(instance=job)

    return render(
        request,
        "planners/planner_home.html",
        {
            "job": job,
            "add_job_form": new_job,
            "edit_job_form": edit_job
        }
    )


def job_delete(request, job_id):
    """
    Deletes a Job.

    **Context**

    ``job``
        An instance of :model:`tradesman.job`.
    """
    job = get_object_or_404(Job, pk=job_id)

    job.delete()
    messages.add_message(
        request,
        messages.SUCCESS,
        'Job deleted!'
    )

    return HttpResponseRedirect(reverse('planner_home'))


@login_required
def user_detail(request, slug):
    """
    Renders the user detail page
    and handles any POST requests from the
    forms used to updating the UserProfile page.
    """
    queryset = UserProfile.objects.all()
    user = get_object_or_404(queryset, slug=slug)

    if request.method == "POST":
        # Checks if the form submitted
        # is the contact details or user details forms.
        if 'update_contact_details' in request.POST:
            update_contact_details_form = (
                UpdateContactDetailsForm(request.POST, instance=user))
            # Saves the form if it is valid.
            if update_contact_details_form.is_valid():
                update_contact_details_form.save()
                messages.add_message(
                    request, messages.SUCCESS,
                    'Contact details updated successfully.'
                )
            else:
                messages.add_message(
                    request, messages.ERROR,
                    'Failed to update contact details.'
                    'Please check the form.'
                )
        elif 'update_user_details' in request.POST:
            update_user_details_form = (
                UpdateUserDetailsForm(request.POST, instance=user))
            # Saves the form if it is valid.
            if update_user_details_form.is_valid():
                update_user_details_form.save()
                messages.add_message(
                    request, messages.SUCCESS,
                    'User details updated successfully.'
                )
            else:
                messages.add_message(
                    request, messages.ERROR,
                    'Failed to update user details.'
                    'Please check the form.'
                )

    update_contact_details_form = (
        UpdateContactDetailsForm(instance=user))
    update_user_details_form = (
        UpdateUserDetailsForm(instance=user))

    return render(
        request,
        "planners/user_detail.html",
        {
            "user_profile": user,
            "contact_form": update_contact_details_form,
            "user_details_form": update_user_details_form,
        },
    )


def add_user(request):
    """
    Renders the add user page and handles the
    POST requests from new user form.
    """
    if request.method == "POST":
        user = request.user
        # Checks if the user had a userprofile.
        if hasattr(user, 'userprofile'):
            form = NewUserForm(instance=user.user_profile)
            if form.is_valid():
                form.save()
                messages.success(request, 'New User Added!')
                # You could return a redirect to a success page
                return HttpResponseRedirect(reverse('planner_home'))
            else:
                messages.error(
                    request,
                    'Failed to add new user. Please check the form.'
                )
        else:
            new_user_form = NewUserForm(data=request.POST)
            if new_user_form.is_valid():
                new_user_form.save(commit=False)
                new_user_form.instance.slug = UserProfile.generate_slug(
                    new_user_form.instance)
                new_user_form.save()
                messages.success(request, 'New User Added!')
                # You could return a redirect to a success page
                return HttpResponseRedirect(reverse('planner_home'))

    else:
        new_user_form = NewUserForm()

    return render(
        request,
        "planners/add_user.html",
        {
            "new_user_form": new_user_form,
        },
    )
