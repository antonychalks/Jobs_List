from main.models import UserProfile
from django import forms


class UpdateContactDetailsForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('email', 'phone', 'other_phone', 'address', 'postcode', 'emergency_name', 'emergency_number', )
        
class UpdateUserDetailsForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('trade', 'certifications', 'medical')
        
class NewUserForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('user', 'role', 'fname', 'lname', 'slug', 'email', 'phone', 'other_phone', 'address', 'postcode', 'medical', 'emergency_name', 'emergency_number', 'trade', 'certifications')