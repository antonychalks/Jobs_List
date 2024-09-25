from django import forms
from .models import Job, Task


class JobAdminForm(forms.ModelForm):
    """ Creates the form for editing a job the admin panel"""
    class Meta:
        model = Job
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Limit choices for created_by field to users with role=0
        self.fields['created_by'].queryset = (
            self.fields['created_by'].queryset.filter(userprofile__role=0)
        )


class UpdateJobContactDetailsForm(forms.ModelForm):
    """ Form for updating a jobs contact details. """
    class Meta:
        model = Job
        fields = (
            'customer_name',
            'phone',
            'other_phone',
            'email',
            'street',
            'town_city',
            'county',
            'postcode'
        )


class AddTaskForm(forms.ModelForm):
    """ Form for adding a new task to the database. """
    class Meta:
        model = Task
        fields = ('id',
                  'description',
                  'trades_required',
                  'time_required',
                  'is_completed'
                  )


class EditTaskForm(forms.ModelForm):
    """ Form for editing a task in the database. """
    class Meta:
        model = Task
        fields = (
            'description',
            'trades_required',
            'time_required',
            'is_completed'
        )


class AssignTradesmanForm(forms.ModelForm):
    """ Form for assigning a tradesman to a task. """
    class Meta:
        model = Task
        fields = ('tradesman_assigned',)
