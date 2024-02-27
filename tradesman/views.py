from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Job
from .forms import UpdateJobContactDetailsForm, NewJobForm
from django.contrib import messages
from planners.views import user_detail

# Create your views here.
class tradesman_home(generic.ListView):
    queryset = Job.objects.all()
    context_object_name = 'Job_List'
    template_name = "tradesman/tradesman_home.html"
    paginate_by = 6
    
def view_job(request):
        return render(
        request,
        "tradesman/job_detail.html",
    )
        
        
def job_detail(request, slug):
    job = get_object_or_404(Job, slug=slug)
    context_object_name = 'Job'
    if request.method == "POST":
        form = UpdateJobContactDetailsForm(request.POST, instance=job)
        if form.is_valid():
            form.save()
            messages.success(request, 'Customer details updated successfully.')
        else:
            messages.error(request, 'Failed to update user details. Please check the form.')
    else:
        form = UpdateJobContactDetailsForm(instance=job)

    return render(
        request,
        "tradesman/job_detail.html",
        {
            "job": job,
            "update_job_contact_details_form": form,
        },
    )