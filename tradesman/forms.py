from django import forms
from .models import Job, Task

class JobAdminForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Limit choices for created_by field to users with role=0
        self.fields['created_by'].queryset = self.fields['created_by'].queryset.filter(userprofile__role=0)
        
class UpdateJobContactDetailsForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ('customer_name','phone', 'other_phone', 'email', 'street', 'town_city', 'county', 'postcode')
        
        
class NewJobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = '__all__'
        
class AddTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('id', 'description', 'trades_required', 'is_completed')