from main.models import UserProfile
from django.contrib.auth.models import User
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Submit
from main.models import TRADES, ROLE
from tradesman.models import Job


class UpdateContactDetailsForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('email', 'phone', 'other_phone', 'street', 'town_city', 'county', 'postcode', 'nok', 'nok_number', )
        
class UpdateUserDetailsForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('profile_image','role', 'trade', 'certifications', 'medical')
        
        
class NewUserForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = '__all__'
        
class NewJobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ('customer_name', 'phone', 'other_phone', 'email', 'street', 'town_city', 'county', 'postcode', 'job_description')
        
class EditJobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ('customer_name', 'phone', 'other_phone', 'email', 'street', 'town_city', 'county', 'postcode', 'job_description')