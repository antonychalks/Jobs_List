from main.models import UserProfile
from django import forms
from tradesman.models import Job


class UpdateContactDetailsForm(forms.ModelForm):
    """ Form for updating contact details """
    class Meta:
        model = UserProfile
        fields = (
            'email',
            'phone',
            'other_phone',
            'street',
            'town_city',
            'county',
            'postcode',
            'nok',
            'nok_number',
        )


class UpdateUserDetailsForm(forms.ModelForm):
    """ Form for updating user details """
    class Meta:
        model = UserProfile
        fields = (
            'profile_image',
            'role',
            'trade',
            'certifications',
            'medical'
        )


class NewUserForm(forms.ModelForm):
    """ Form for creating new user """
    class Meta:
        model = UserProfile
        fields = '__all__'
        exclude = ['slug', 'profile_complete', 'is_initial_signup']


class NewJobForm(forms.ModelForm):
    """ Form for creating new job """
    class Meta:
        model = Job
        fields = ('customer_name', 'phone', 'other_phone', 'email', 'street',
                  'town_city', 'county', 'postcode', 'job_description')


class EditJobForm(forms.ModelForm):
    """ Form for editing job details """
    class Meta:
        model = Job
        fields = ('customer_name', 'phone', 'other_phone', 'email', 'street',
                  'town_city', 'county', 'postcode', 'job_description')
