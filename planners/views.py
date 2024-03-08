from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib import messages
from main.models import UserProfile as UserProfile
from tradesman.models import Job, Task
from .forms import UpdateContactDetailsForm, UpdateUserDetailsForm, NewUserForm, NewJobForm, EditJobForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def planner_home(request):
    job = Job.objects.all()
    new_job = NewJobForm()
    edit_job = EditJobForm()
    
    return render(
        request,
        "planners/planner_home.html",
        {
            "job": job,
            "add_job_form": new_job,
            "edit_job_form" : edit_job,
        }
    )
    
class UserList(generic.ListView):
    queryset = UserProfile.objects.all()
    context_object_name = 'UserList'
    template_name = "planners/list_tradesman.html"
    paginate_by = 6

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