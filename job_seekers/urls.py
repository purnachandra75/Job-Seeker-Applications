from django.urls import path
from . import views 
urlpatterns=[
    path('Homepage/',views.getHomepage,name='JobsekerHomepage'),
    
    path('createprofile/',views.createprofile,name='createprofile'),
    path('viewprofile/',views.viewProfile,name='Viewprofile'),
    path('updateEducation/<int:id> ',views.updateEducation , name='updateEducation'),
    path('delete/<int:pk>',views.delete,name='delete'),
    path('update/<int:pk>/<int:uid>',views.update,name='update'),
    path('add/<int:uid>/',views.add , name='add'),
    path('updateskill/<int:uid>',views.updateSkill, name='updateskill'),
    path('addskills/',views.addskills,name='addskills'),
    path('deleteskill/<int:uid>',views.deleteskills,name='deleteskills'),
    path('updatenewskill/<int:pk>/<int:uid>',views.updateNewSkill,name='updatenewskill'),
    path('updateWorkExp/<int:uid>',views.updateworkexp,name='updateWorkExp'),
    path('addworkexp/',views.addworkexp,name='addworkexp'),
    path('deleteworkExp/<int:pk>',views.deleteworkexp,name='deleteworkExp'),
    path('updatenewWorkExp/<int:pk>/<int:uid>',views.updatenewworkexp,name='updatenewWorkExp'),
    path('updatelang/<int:uid>',views.updateLang, name='updatelang'),
    path('addlang/',views.addlang,name='addlang'),
    path('deletelang/<int:pk>',views.deletelang,name='deletelang'),
    path('updatenewlang/<int:pk>/<int:uid>/',views.updateNewlang,name='updatenewlang'),
    path('applicants/<int:jobid>/<int:uid>/',views.applicants,name='applicant'),
    path('appliedjobs/<int:uid>/',views.applidjoblist,name='appliedjobs')
]