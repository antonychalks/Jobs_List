from main.models import UserProfile
from django.contrib.auth.models import User
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Submit
from main.models import TRADES, ROLE
from tradesman.models import Job


class InitialSignUpForm(forms.ModelForm):
    """Form for the user to submit their details on initial sign up."""

    class Meta:
        model = UserProfile
        fields = ('fname', 'lname', 'email', 'phone', 'role', 'trade')
