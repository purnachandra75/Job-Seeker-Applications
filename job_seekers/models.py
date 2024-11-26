from django.db import models
from django.contrib.auth.models import User
from usercredintials.models import Userdetails 
import re
from Employeers.models import JobPost
from pydantic import ValidationError

def validate_phone_number(value):
    pattern = r'^\+?1?\d{9,15}$'
    if not re.match(pattern, value):
        raise ValidationError('Invalid phone number. Please enter a valid number.')

# Create your models here.
class Personalinfo(models.Model):
    user = models.OneToOneField(Userdetails, on_delete=models.CASCADE)
    Name=models.CharField(max_length=40,blank=False)
    Email=models.EmailField(blank=False,unique=True)
    Phone_no=models.CharField(blank=False,validators=[validate_phone_number],max_length=15)
    Addres=models.TextField()
    career_obj=models.TextField(null=True)
    profile_status_choices = [
        ('active', 'Active'),
        ('inactive', 'Inactive'),
    ]
    profile_status = models.CharField(max_length=8, choices=profile_status_choices, default='inactive')
    def __str__(self):
        return f'personalinfo  Name: {self.Name}, Email: {self.Email}, Phone: {self.Phone_no}'

class Education(models.Model):
    User=models.ForeignKey(Personalinfo,on_delete=models.CASCADE)
    degree_choise=[('B.tech','B.tech'),("M.tech",'M.tech')]
    Degree=models.CharField(max_length=40,choices=degree_choise)
    Institute_name=models.CharField(max_length=40,blank=False)
    StartDate=models.DateField()
    EndDate=models.DateField()
class WorkExperience(models.Model):
    User=models.ForeignKey(Personalinfo,on_delete=models.CASCADE)
    title_choice=[('software engineering','software engineering'),('markating manager','markating manager'),('coustomer service','coustomer service')]
    Title=models.CharField(max_length=40,choices=title_choice)
    Project_name=models.TextField(max_length=100,blank=False)
    Company_name=models.CharField(max_length=40,blank=False)
    Technology=models.CharField(max_length=40,blank=False)
    StartDate=models.DateField()
    EndDate=models.DateField()
class Skill(models.Model):
    User=models.ForeignKey(Personalinfo,on_delete=models.CASCADE)
    Skillname=models.CharField(max_length=40,blank=False)
    choice=[('biggner','biggner'),('intermediat','intermediat'),('advance','advance'),('Expart','Expart')]
    Proficiency=models.CharField(max_length=40,blank=False,choices=choice)
    YearofExperiance=models.IntegerField()



class Languages(models.Model):
    User=models.ForeignKey(Personalinfo,on_delete=models.CASCADE)
    LanguageName=models.CharField(max_length=40,blank=False)
    proficiency_choice=[('biggner','biggner'),('intermediat','intermediat'),('advance','advance')]
    Proficiency=models.CharField(max_length=40,blank=False,choices=proficiency_choice)
    Can_Read=models.BooleanField(default=False)
    Can_Speak=models.BooleanField (default=False)
    Can_Write=models.BooleanField(default=False)
   

class Applicant(models.Model):
    Job=models.ForeignKey(JobPost,on_delete=models.CASCADE)
    seeker=models.ForeignKey(Personalinfo,on_delete=models.CASCADE)