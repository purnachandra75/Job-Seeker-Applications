from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.loginpage,name='loginpage'),
    path('registration',views.Registration.as_view(),name='registration')
    
]