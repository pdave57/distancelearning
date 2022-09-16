from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import CreateUserForm, ProfileForm,CourseRegistrationForm
from .models import *

def index(request):   
    authors = Authors.objects.select_related('courses').all()
    context = {"authors":authors}
    return render(request, 'index.html', context)


def dashboard(request):    
    return render(request, 'account/dashboard.html')

def register(request):
    form = CreateUserForm()    
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data('username')
            messages.success(request, 'account create successful for '+ user)
            return redirect('dashboard')
            
    context = {"form":form}
    return render(request, 'account/register.html', context)

def loginpage(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('account/dashboard')
        else:
            messages.info(request, 'User name Or password is incorrect')
        
    return render(request, 'account/login.html')

def logoutUser(request):
    logout(request)
    return redirect('index')

def createprofile(request):
    form = ProfileForm()
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('account/dashboard')
    context = {'form':form}
    return render(request, "account/profile.html", context)

def editprofile(request, pk):
    profile = Profile.objects.get(id=pk)
    form = ProfileForm(instance=profile)
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('account/dashboard')
    context ={'form':form}
    return render(request, "account/profile.html", context)

def course_registration(request):
    form = CourseRegistrationForm()
    if request.method =="POST":
        form = CourseRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('account/dashboard')
    context = {'form':form}    
    return render(request, "account/course_registration.html", context)

def update_course_registration(request):
    return render(request, "account/course_registration.html")

def course_detail(request, pk):
    profile = Authors.objects.select_related('courses').filter(id=pk)
    context = {"profile":profile}
    return render(request, "account/course_detail.html", context)

def contact(request):
    return render(request, 'contactus.html')