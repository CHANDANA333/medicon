
from django.shortcuts import render
from django.http import HttpResponse
from .models import user
# Create your views here.

def welcome(request):
    return render(request,'index.html' )

def login(request):
    if(request.method == "POST"):
        name = request.POST['name']
        password = request.POST['password']
        user_obj = user.objects.filter(name=name, password=password).exists()
        if user_obj :
            return HttpResponse("Login Success")
        else:
            return render(request,'register.html' , {
                'message' : 'Mundu register Avvu'
            })
    else:
        return render(request,'login.html')

def register(request):
    if request.method == "POST":
        name = request.POST['name']
        if name is None or name == "":
            return render(request,'register.html', {"message" : "Name is required"} )
        password = request.POST['password']
        user.objects.create(name=name, password=password)
        return render(request,'login.html', {
            "message" : "Register success, ipdu login avvu"
        })
    else:
        return render(request,'register.html')
        