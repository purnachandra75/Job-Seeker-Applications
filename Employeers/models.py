from django.db import models
from django.db import models
from usercredintials.models import Userdetails
class Employer(models.Model):
    INDUSTRY_CHOICES = [
        ('IT', 'Information Technology'),
        ('Sales', 'Sales'),
        ('Medical', 'Medical'),
        ('Marketing', 'Marketing'),
    ]
    user = models.OneToOneField(Userdetails, on_delete=models.CASCADE)
    company_name = models.CharField(blank=False,max_length=255)
    industry = models.CharField(max_length=50, choices=INDUSTRY_CHOICES)
    description = models.TextField(blank=True, null=True)
    
    # Contact Information
    full_name = models.CharField(blank=False,max_length=255)
    email = models.EmailField(blank=False,unique=True)
    phone_number = models.CharField(blank=False,max_length=20)
    
    def __str__(self):
        return self.company_name

class Employers(models.Model):
    INDUSTRY_CHOICES = [
        ('IT', 'Information Technology'),
        ('Sales', 'Sales'),
        ('Medical', 'Medical'),
        ('Marketing', 'Marketing'),
    ]
    user = models.OneToOneField(Userdetails, on_delete=models.CASCADE)
    company_name = models.CharField(blank=False,max_length=255)
    industry = models.CharField(max_length=50, choices=INDUSTRY_CHOICES)
    description = models.TextField(blank=True, null=True)
    
    # Contact Information
    full_name = models.CharField(blank=False,max_length=255)
    email = models.EmailField(blank=False,unique=True)
    phone_number = models.CharField(blank=False,max_length=20)
    
    def __str__(self):
        return self.company_name
class JobPost(models.Model):
    JOB_TYPE_CHOICES = [
        ('Full-Time', 'Full-Time'),
        ('Part-Time', 'Part-Time'),
        ('Contract', 'Contract'),
        ('Internship', 'Internship'),
    ]

    EXPERIENCE_CHOICES = [
        ('0-2 years', '0-2 years'),
        ('3-5 years', '3-5 years'),
        ('5-8 years', '5-8 years'),
    ]

    employer = models.ForeignKey(Employer, on_delete=models.CASCADE, related_name='jobs')
    title = models.CharField(blank=False,max_length=255)
    description = models.TextField(blank=False)
    job_type = models.CharField(blank=False,max_length=50, choices=JOB_TYPE_CHOICES)
    salary_min = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    salary_max = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    location = models.CharField(blank=False,max_length=255)
    required_skills = models.CharField(blank=False,max_length=255)
    experience = models.CharField(max_length=20, choices=EXPERIENCE_CHOICES)
    remote_work = models.BooleanField(default=False)

    def __str__(self):
        return self.title


# Create your models here.
