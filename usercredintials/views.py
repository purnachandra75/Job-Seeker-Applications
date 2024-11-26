import random
import re
from typing import Any
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from .models import Userdetails
from .forms import UserdetailsForm
from django.views import View
from django.core.mail import send_mail


# Create your views here.
def loginpage(request):
    if request.method=='GET':
        return render(request,'login.html')
    if request.method == 'POST':
        email=request.POST['email']
        password=request.POST['password']
        somedata=Userdetails.objects.filter(Email=email,Password=password)
        print(somedata)
        if not somedata:
            return render(request,'login.html',{'err':'invalid username or password'})
        else:

            request.session['user'] = somedata[0].Last_name
            request.session['uid']=somedata[0].id
            
            if somedata[0].category == 'Employer':
                #return render(request,'employerHomepage.html',{'user':somedata[0].Last_name})
                return redirect('homepage')
            if somedata[0].category =='Jobseeker':
                return redirect('JobsekerHomepage')
class Registration(View):
    def get(self, request):
        
        return render(request, 'Registration.html', {'form': UserdetailsForm()})

    def post(self, request):
        form = UserdetailsForm(request.POST)
        password=request.POST['Password']
        confpass=request.POST['confpass']
        
       
        data=Userdetails.objects.filter(Email=request.POST['Email'])
        if data:
            return render(request,'Registration.html', {'form':form ,'has_error':'email already exist...!!'})
        if password != confpass:
            return render(request, 'Registration.html', {'form':form ,'has_error':'password does not match'})
        
        elif form.is_valid():
            form.save()
            return render(request, 'successful.html')
        else:
            # Pass the form with errors back to the template
            return render(request, 'Registration.html', {'form': form})
        
# class Forgotpass(View):

#     def get(self,request):
#         return render(request,'forgotpass.html')
#     def post(self,request):
        
#         email=request.POST['email']
        
#         data=Userdetails.objects.filter(Email=email)
#         if not data:
#             return render(request,'forgotpass.html',{'msg':'the email does not exist .....!!\nplease register ....!!\n'})
#         else:

#             return redirect('validpass',email=email)
# class Changepass(View):
#     def get(self,request,email):
#         return render(request,'changepass.html')
#     def post(self,request,email):
#         password=request.POST['password']
#         confpass=request.POST['confpassword']
#         if len(password) < 8:
#             return render(request,'changepass.html',{'msg':"Password must be at least 8 characters long."})
#         if not re.search(r'[A-Za-z]', password) or not re.search(r'[0-9]', password):
#             return render(request,'changepass.html',{'msg':"Password must contain both letters and numbers."})

#         if password != confpass:
#             return render(request,'changepass.html',{'msg':'password does not match'})
#         else:
#             password=request.POST['password']
#             somedata=Userdetails.objects.get(Email=email) 
#             somedata.Password=password
            
#             somedata.save()
#             return render(request,'successful.html',{'msg':'successfuly change password...!!!'})



# class Validmail(View):
#     def randomnum(self):
#         # Generate and save OTP to session
#         random_number = random.randint(000000, 999999)
#         self.request.session['random_number'] = random_number  # Store in session
#         return random_number
    
#     def get(self, request, email):
        
#         random_number = self.randomnum()
#         print('Generated OTP:', random_number)
#         send_mail(
#             'Django Verification Code',
#             f'Your verification code is: {random_number}',
#             'purnachandrareddy1602@gmail.com',  
#             [email],  
#         )
#         return render(request, 'verification.html', {'mail': email})
    
#     def post(self, request, email):
#         otp = request.POST.get('otp')
#         saved_otp = self.request.session.get('random_number')  
#         print('Submitted OTP:', otp)
#         print('Saved OTP:', saved_otp)
        
#         if saved_otp is not None and int(otp) == saved_otp:
            
#             del self.request.session['random_number']
#             return redirect('changepass', email=email)
#         else:
            
#             return render(request, 'verification.html', {'mail': email, 'msg': 'Please enter the correct OTP.'})

        

# def logout(request):
#     request.session.flush()
#     return redirect('loginpage')
        