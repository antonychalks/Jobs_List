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

        elif 'add_task' in request.POST:
            if task_formset.is_valid():
                instances = task_formset.save(commit=False)
                for instance in instances:
                    instance.job = job
                    instance.save()
                messages.success(request, 'New task(s) added successfully.')
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
 
def task_edit(request, task_id):
    """
    Display an individual comment for edit.

    **Context**

    ``post``
        An instance of :model:`blog.Post`.
    ``comment``
        A single comment related to the post.
    ``comment_form``
        An instance of :form:`blog.CommentForm`
    """
    job_slug = task.job.slug
    job = get_object_or_404(Job, slug=job_slug)
    task = get_object_or_404(Task, pk=task_id)
    

    if request.method == "POST":
        add_task_form = AddTaskForm(data=request.POST, instance=task)

        if add_task_form.is_valid():
            task = add_task_form.save(commit=False)
            task.job = job
            task.save()
            messages.success(request, 'Task Updated!')
            return HttpResponseRedirect(reverse('post_detail', args=[slug]))
    else:
        add_task_form = AddTaskForm(instance=task)

    return render(request, 'your_template.html', {'add_task_form': add_task_form})
    
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