from django.shortcuts import render, HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import redirect,render
from . models import *
from django.contrib.auth import login ,logout, authenticate
from django.contrib.auth.forms import UserCreationForm 
from django.contrib import messages
from home.models import Blogs


# Create your views here.
def index(request):
    return render(request,'index.html')

def home(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def services(request):
    return render(request,'services.html')

def contact(request):
    if request.method == "POST":
        name = request.POST["name"]
        number = request.POST["number"]
        email = request.POST["email"]
        message = request.POST["message"]


        
    return render(request,'contact.html')

def blogs(request):
    return render(request,'blogs.html')

def login(request):
    
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        
        user = authenticate(email=email,password=password)
        
        if user is not None:
            login(request, user)
            firstname=user.firstname
            return render(request,"index.html", {'firstname':firstname} )
        else:
            messages.error(request, "bad credentials")
            return redirect("/home")

    return render(request,'login.html')

def signup(request):
    
    if request.method =="POST":
        firstname = request.POST["firstname"]
        lastname = request.POST["lastname"]
        email = request.POST["email"]
        password = request.POST["password"]
        cpassword = request.POST["cpassword"]
        
        myuser = User.objects.create_user(email,email,password)
        
        myuser.first_name = firstname
        myuser.last_name = lastname
        
        myuser.save()
        messages.success(request, "Your account is successfully created")
        
        return redirect("/login")
        
        
        
    return render(request,'signup.html')

def signout(request):
    logout(request)
    messages.success(request, "Logged out successfully")
    return render(request,'index.html')
