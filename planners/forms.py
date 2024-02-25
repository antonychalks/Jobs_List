from main.models import UserProfile
from django import forms


class UpdateUserPersonalForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('email', 'phone', 'other_phone', 'address', 'postcode', 'medical', 'emergency_name', 'emergency_number', )
        
class UpdateUserProffessionalForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('trade', 'certifications')
        
class NewUserForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('user','role', 'fname', 'lname', 'slug', 'email', 'phone', 'other_phone', 'address', 'postcode', 'medical', 'emergency_name', 'emergency_number', 'trade', 'certifications')