from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, reverse
from django.forms import modelformset_factory
from django.views import generic
from django.http import HttpResponseRedirect
from django.contrib import messages
from .models import Job, Task
from main.models import UserProfile
from .forms import (
    UpdateJobContactDetailsForm,
    AddTaskForm,
    EditTaskForm,
    AssignTradesmanForm
)


# Create your views here.
class Tradesman_Home(LoginRequiredMixin, generic.ListView):
    """ Renders the tradesman's home page. '"""
    queryset = Job.objects.all()
    context_object_name = 'Job_List'
    template_name = "tradesman/tradesman_home.html"
    paginate_by = 6

    def get_context_data(self, **kwargs):
        """ Apply the context to the tradesman's home page. '"""
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context['users_jobs'] = (
            Job.objects.filter(Tasks__tradesman_assigned__user=user).distinct()
        )
        return context


@login_required
def view_job(request):
    """ Renders the view for each job. """
    user = UserProfile

    return render(
        request,
        "tradesman/job_detail.html",
        {
            "user": user,
        },
    )


@login_required
def job_detail(request, slug):
    """ Renders the job's details page. '"""
    job = get_object_or_404(Job, slug=slug)
    TaskFormSet = modelformset_factory(Task, form=AddTaskForm, extra=1)

    if request.method == "POST":
        contactDetailsForm = (
            UpdateJobContactDetailsForm(request.POST, instance=job)
        )
        task_formset = TaskFormSet(
            request.POST,
            queryset=Task.objects.filter(job=job)
        )
        # Handles the form for updating the job details.
        if ('update_job_contact_details'
                in request.POST
                and contactDetailsForm.is_valid()):
            contactDetailsForm.save()
            messages.success(request, 'Customer details updated successfully.')
            # Redirect after successful form submission
            return HttpResponseRedirect(reverse('job_detail', args=[slug]))
        # Handles the form for adding a new task to a Job
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
                messages.error(request, 'There was an error adding task(s).')

    else:
        contact_details_form = UpdateJobContactDetailsForm(instance=job)
        task_formset = TaskFormSet(queryset=Task.objects.none())

    edit_task = EditTaskForm()
    assign_tradesman = AssignTradesmanForm()
    tradesmen = UserProfile.objects.filter(role=1)

    return render(
        request,
        "tradesman/job_detail.html",
        {
            "job": job,
            "update_job_contact_details_form": contact_details_form,
            "task_formset": task_formset,
            "edit_task": edit_task,
            "assign_tradesman": assign_tradesman,
            "tradesmen": tradesmen,
        },
    )


@login_required
def task_edit(request, task_id, slug):
    """
    Display an individual task for editing.
    """
    # Retrieve the task instance
    task = get_object_or_404(Task, pk=task_id)
    # Retrieve the job instance
    job = get_object_or_404(Job, slug=slug)

    if request.method == "POST":
        # Initialize form with task instance and data from request
        edit_task_form = EditTaskForm(data=request.POST, instance=task)
        if edit_task_form.is_valid():
            # Save the form data to the task instance
            task = edit_task_form.save(commit=False)
            task.job = job
            task.save()

            messages.success(request, 'Task Updated!')
            return HttpResponseRedirect(reverse('job_detail', args=[slug]))
        else:
            messages.error(request, 'Error updating task!')
    else:
        # Initialize form with task instance
        edit_task_form = EditTaskForm(instance=task)

    add_task_form = AddTaskForm(instance=task)
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


@login_required
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


@login_required
def assign_tradesmen(request, slug, task_id):
    """ A view to assign tradesman to an individual task. """
    queryset = Job.objects.all()
    task = get_object_or_404(Task, pk=task_id)
    job = get_object_or_404(queryset, slug=slug)

    # Handles the POST request when assigning a tradesman.
    if request.method == "POST":
        tradesman_form = AssignTradesmanForm(request.POST)
        if tradesman_form.is_valid():
            tradesman = tradesman_form.cleaned_data['tradesman_assigned']
            task.tradesman_assigned.set(tradesman)
            task.job.status = Job.set_job_status(task.job)
            task.save()
            messages.success(request, 'Tradesman assigned successfully.')
            return HttpResponseRedirect(reverse('job_detail', args=[slug]))
    else:
        tradesman_form = AssignTradesmanForm()

    return render(
        request,
        "tradesman/job_detail.html",
        {
            "job": job,
            "tradesman_form": tradesman_form,
        },
    )
