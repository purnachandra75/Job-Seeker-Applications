from django import forms
from .models import Employer,JobPost

class EmployerForm(forms.ModelForm):
    class Meta:
        model=Employer
        fields=['full_name','email','phone_number','company_name','industry','description']

class JobpostForm(forms.ModelForm):
    class Meta:
        model=JobPost
       
        exclude=['employer']