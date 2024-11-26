from django import forms
from .models import Userdetails
from django.core.exceptions import ValidationError
class UserdetailsForm(forms.ModelForm):
    class Meta:
        model = Userdetails
        fields =['Email','First_name','Last_name','Phone_Number','Password','category']
        