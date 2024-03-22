from django.urls import path
from  patientapp.views import *


urlpatterns = [

    #User Signin,Signup,Logout,IndexpagenIndexpage1
    
    path('patientapp/',signin,name="signin"),
    path('signup/',signup,name="signup"),
    path('logout/',logout,name='logout'),
    path('appointment/',book_appointment,name='book_appointment'),
    path('show_appointment/',show_appo,name='show_appointment'),

    
    
]