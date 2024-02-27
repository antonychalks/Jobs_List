from main.models import UserProfile
from django.contrib.auth.models import User
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Submit
from main.models import TRADES, ROLE


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
        