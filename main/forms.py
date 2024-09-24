from main.models import UserProfile
from django import forms


class InitialSignUpForm(forms.ModelForm):
    """Form for the user to submit their details on initial sign up."""

    class Meta:
        model = UserProfile
        fields = ('fname', 'lname', 'email', 'phone', 'role', 'trade')
