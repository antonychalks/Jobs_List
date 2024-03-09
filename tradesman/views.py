from django.core.cache import cache
from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.forms import modelformset_factory
from django.views import generic
from django.http import HttpResponseRedirect
from django.contrib import messages
from planners.views import job_status
from .models import Job, Task
from .forms import UpdateJobContactDetailsForm, AddTaskForm, EditTaskForm
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

        elif 'add_task' in request.POST:
            if task_formset.is_valid():
                instances = task_formset.save(commit=False)
                for instance in instances:
                    instance.job = job
                    instance.save()
                    update_job_status(job)
                messages.success(request, 'New task(s) added successfully.')
                # Redirect after successful form submission
                return HttpResponseRedirect(reverse('job_detail', args=[slug]))
    
    else:
        contactDetailsForm = UpdateJobContactDetailsForm(instance=job)
        task_formset = TaskFormSet(queryset=Task.objects.none())
        
    edit_task = EditTaskForm()
    
    return render(
        request,
        "tradesman/job_detail.html",
        {
            "job": job,
            "update_job_contact_details_form": contactDetailsForm,
            "task_formset": task_formset,
            "edit_task": edit_task,
        },
    )
 
def task_edit(request, task_id, slug):
    """
    Display an individual task for editing.
    """
    # Retrieve the task instance
    task = get_object_or_404(Task, pk=task_id)
    # Retrieve the job instance
    job = get_object_or_404(Job, slug=slug)
    
    if request.method == "POST":
        # Print out the request.POST dictionary to inspect the data
        print(request.POST)
        
        # Initialize form with task instance and data from request
        edit_task_form = EditTaskForm(data=request.POST, instance=task)
        if edit_task_form.is_valid():
            # Save the form data to the task instance
            task = edit_task_form.save(commit=False)
            task.job = job
            task.save()
            
            update_job_status(job)
            
            messages.success(request, 'Task Updated!')
            return HttpResponseRedirect(reverse('job_detail', args=[slug]))
        else:
            messages.error(request, 'Error updating task!')
    else:
        # Initialize form with task instance
        edit_task_form = EditTaskForm(instance=task)
        print(edit_task_form.errors)
        print(request.POST)

    add_task_form = AddTaskForm(instance=task)
    
    # If the code reaches here, it means it's a GET request or form submission failed
    return render(
        request,
        "tradesman/job_detail.html",
        {
            "add_task_form": add_task_form,  # Pass the form to the template
            "job": job,
            "edit_task_form": edit_task_form
            # Other context variables you may need
        },
    )

def update_job_status(job):
    # Get all tasks associated with the job
    tasks = job.Tasks.all()
    
    job.status = job_status(job)
    
    # Save the updated job status
    job.save()
        
def task_delete(request, slug, task_id):
    """
    Delete an individual comment.

    **Context**

    ``post``
        An instance of :model:`blog.Post`.
    ``comment``
        A single comment related to the post.
    """
    queryset = Job.objects.all()
    job = get_object_or_404(queryset, slug=slug)
    task = get_object_or_404(Task, pk=task_id)

    task.delete()
    messages.add_message(request, messages.SUCCESS, 'Task deleted!')

    return HttpResponseRedirect(reverse('job_detail', args=[slug]))

