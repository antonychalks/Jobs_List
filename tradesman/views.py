from django.core.cache import cache
from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.forms import modelformset_factory
from django.views import generic
from django.http import HttpResponseRedirect
from django.contrib import messages
from .models import Job, Task
from .forms import UpdateJobContactDetailsForm, NewJobForm, AddTaskForm
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
    TaskFormSet = modelformset_factory(Task, form=AddTaskForm, extra=1)

    if request.method == "POST":
        contactDetailsForm = UpdateJobContactDetailsForm(request.POST, instance=job)
        task_formset = TaskFormSet(request.POST, queryset=Task.objects.filter(job=job))

        if 'update_job_contact_details' in request.POST and contactDetailsForm.is_valid():
            contactDetailsForm.save()
            messages.success(request, 'Customer details updated successfully.')
            # Redirect after successful form submission
            return HttpResponseRedirect(reverse('job_detail', args=[slug]))

        elif 'add_task' in request.POST and task_formset.is_valid():
            instances = task_formset.save(commit=False)
            for instance in instances:
                instance.job = job
                instance.save()
            messages.success(request, 'Task(s) added successfully.')
            # Redirect after successful form submission
            return HttpResponseRedirect(reverse('job_detail', args=[slug]))
    else:
        contactDetailsForm = UpdateJobContactDetailsForm(instance=job)
        task_formset = TaskFormSet(queryset=Task.objects.none())

    return render(
        request,
        "tradesman/job_detail.html",
        {
            "job": job,
            "update_job_contact_details_form": contactDetailsForm,
            "task_formset": task_formset,
        },
    )
    
def task_delete(request, slug, task_id):
    """
    Delete an individual task.

    **Context**

    ``job``
        An instance of :model:`tradesman.Job`.
    ``task``
        A single task related to the job.
    """
    job_instance = get_object_or_404(Job, slug=slug)
    task_instance = get_object_or_404(Task, pk=task_id)
    
    task_instance.delete()
    messages.success(request, 'Task deleted!')

    cache.clear
    
    # Redirect after successful deletion
    return redirect('job_detail', slug=slug)