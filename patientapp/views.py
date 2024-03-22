from django.shortcuts import render

# Create your views here.

from django.shortcuts import render,redirect




# from practice.decorator import status


# User signin 
def signin(request):
    return render(request,'userlogin.html')

#User logout
def logout(request):
    return redirect('user:signin')



# User register
def signup(request):
    return render(request,'usersignup_1.html')
    




def book_appointment(request):
    return render(request,'appointment1.html')


def show_appo(request):
    return render(request,'appointment_status1.html') 


def view_appo_status(request):
    return render(request,'appointment_status1.html')
