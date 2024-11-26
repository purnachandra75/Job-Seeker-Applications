from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.urls import reverse_lazy
from .forms import EmployerForm,JobpostForm
from .models import Employer,JobPost
from django.views.generic.edit import FormView,CreateView
from django.views.generic.base import TemplateView
from django.views.generic import ListView

from job_seekers.models import Personalinfo,Education,WorkExperience,Languages,Skill,Applicant


def registerEmp(request):
    if request.method =="GET":
        return render(request,'registeremp.html',{'e_form':EmployerForm()})
    if request.method =='POST':
        somedata=EmployerForm(request.POST)
        if somedata.is_valid():
            somedata.save()
            return render(request,'homepage.html')
        return render(request,'registeremp.html',{'e_form':EmployerForm(),'msg':'pelase insert valid data'})

class Homepage(TemplateView):
    template_name='homepage.html' 
    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)   
        print(self.request.session.get('uid'))
        context['user']=self.request.session.get('user')
        context['uid']=self.request.session.get('uid')
        somedata=Employer.objects.get(user_id=self.request.session.get('uid'))
        context['jobdata']=JobPost.objects.filter(employer_id=somedata.id)
        
        return context 
class CreateEmp(FormView):
    
    form_class=EmployerForm
    template_name='createempprofile.html'
    success_url='homepage.html'
    def form_valid(self, Form):
        Form.save(commit=False)

        return super.form_valid(Form)
    
def createProfile(request):
    uid=request.session.get('uid')
    user=request.session.get('user')
    if request.method == 'GET':
        somedata=Employer.objects.filter(user_id=uid)
        if somedata:
            return redirect('viewempprofile')
        else :
            return render(request,'createempprofile.html',{'form':EmployerForm(),'user':user})
    if request.method=='POST':
        somedata=EmployerForm(request.POST)
        if somedata.is_valid():
            newdata=somedata.save(commit=False)
            newdata.user_id=uid
            newdata.save()
            return redirect('homepage')
        return HttpResponse('bad dataa.....')
def updateProfile(request):
    uid=request.session.get('uid')
    user=request.session.get('user')
    if request.method =='GET':
        somedata=Employer.objects.get(user_id=uid)
        return render(request,'createempprofile.html',{'form':EmployerForm(instance=somedata),'user':user})

    if request.method == "POST":
        somedata=Employer.objects.get(user_id=uid)
        somedata=EmployerForm(request.POST,instance=somedata)
        if somedata.is_valid():
            somedata.save()
            return redirect('viewempprofile')
def viewProfile(request):
    uid=request.session.get('uid')
    user=request.session.get('user')
    somedata=Employer.objects.get(user_id=uid)
    return render(request,'viewempprofile.html',{'somedata':somedata,'user':user})
class Createjob(CreateView):
    template_name='createjobpost.html'
    model=JobPost
    fields='__all__'
    exclude=['employer']
    success_url= reverse_lazy('homepage')
    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context['user']=self.request.session.get('user')
        return context

class Viewpostedjobs(TemplateView):

    template_name='listofjobs.html'
    def get_context_data(self, **kwargs): 
        context=super().get_context_data(**kwargs)
        uid=kwargs['uid']
        somedata=Employer.objects.get(user_id=uid)
        context['listofjobs']=JobPost.objects.filter(employer_id=somedata.id)
        context['user']=self.request.session.get('user')
        return context

class Moredetails(TemplateView):
    template_name='moredetails.html'
    def get_context_data(self, **kwargs): 
        context= super().get_context_data(**kwargs)
        uid=kwargs['id']
        context['personalinfo']=Personalinfo.objects.get(id=uid)
        context['eduinfo']=Education.objects.filter(User_id=uid)
        context['skills']=Skill.objects.filter(User_id=uid)
        context['lang']=Languages.objects.filter(User_id=uid)
        context['workexp']=WorkExperience.objects.filter(User_id=uid)
        return context

class Moreabout(TemplateView):
    template_name = 'moredetails.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        hint = kwargs['skill']

        
        somedata = Skill.objects.filter(Skillname=hint)
        info=[]
        for eachone in somedata:
            uid = eachone.User_id
            d={}
            
            d['personal_info']= Personalinfo.objects.filter(id=uid)
            d['education_info'] = Education.objects.filter(User_id=uid)
            d['skills_info'] = Skill.objects.filter(User_id=uid)
            d['languages_info'] = Languages.objects.filter(User_id=uid)
            d['workexp_info'] = WorkExperience.objects.filter(User_id=uid)
            
            info.append(d)
        context['data']=info
        return context

class ListofApplicants(TemplateView):
    template_name='listofApplicants.html'
    def get_context_data(self, **kwargs): 
        contaxt= super().get_context_data(**kwargs)
        jobid=kwargs['jobid']
        somedata=Applicant.objects.filter(Job_id=jobid)
        l=[]
        for eachdata in somedata:
            l.append(Personalinfo.objects.filter(id=eachdata.seeker_id))
        contaxt['apllicants']=l
        contaxt['user']=self.request.session.get('user')
        return contaxt

class AboutJobseeker(TemplateView):
    template_name='aboutjobseeker.html'
    def get_context_data(self, **kwargs): 
        context= super().get_context_data(**kwargs)
        uid=kwargs['id']
        context['personalinfo']=Personalinfo.objects.get(id=uid)
        context['eduinfo']=Education.objects.filter(User_id=uid)
        context['skills']=Skill.objects.filter(User_id=uid)
        context['lang']=Languages.objects.filter(User_id=uid)
        context['workexp']=WorkExperience.objects.filter(User_id=uid)
        context['user']=self.request.session.get('user')
        return context
        
class ListofJobSekers(ListView):
    template_name='listofjobseekers.html'
    model=Personalinfo
    def get_queryset(self) :
        alldata=super().get_queryset()
        res=alldata.filter(profile_status='active')
        user=self.request.session.get('user')
        return res
# Create your views here.
