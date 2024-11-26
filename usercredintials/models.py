import re
from django.db import models
from django.core.exceptions import ValidationError


def validate_password_strength(value):
    if len(value) < 8:
        raise ValidationError("Password must be at least 8 characters long.")
    if not re.search(r'[A-Za-z]', value) or not re.search(r'[0-9]', value):
        raise ValidationError("Password must contain both letters and numbers.")

class Userdetails(models.Model):
    Email=models.EmailField(unique=True,blank=False)
    First_name=models.CharField(max_length=20,blank=False)
    Last_name=models.CharField(max_length=40,blank=False)
    Phone_Number=models.CharField(blank=False,max_length=10)
    Password=models.CharField(blank=False,max_length=20,validators=[validate_password_strength])
    select=[
        ('Employer','Employer'),
        ('Jobseeker','Jobseeker')
    ]
    category=models.CharField(blank=False,max_length=20,choices=select)
    created_at = models.DateTimeField(auto_now_add=True)  
    updated_at = models.DateTimeField(auto_now=True)


    


    
       