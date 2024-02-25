from main.models import UserProfile
from django import forms


class UpdateContactDetailsForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('email', 'phone', 'other_phone', 'street', 'town_city', 'county', 'postcode', 'nok', 'nok_number', )
        
class UpdateUserDetailsForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('role', 'trade', 'certifications', 'medical')
        
class NewUserForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('user', 'role', 'fname', 'lname', 'slug', 'email', 'phone', 'other_phone', 'street', 'town_city', 'county', 'postcode', 'medical', 'nok', 'nok_number', 'trade', 'certifications')