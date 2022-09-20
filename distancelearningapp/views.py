from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .forms import CreateUserForm, ProfileForm,CourseRegistrationForm
from .models import *

def index(request):   
    authors = Authors.objects.select_related('courses').all()
    context = {"authors":authors}
    return render(request, 'index.html', context)

@login_required(login_url='/account/loginpage')
def dashboard(request):
    username = request.session['username']
    user = User.objects.get(username = username)
    profile = Profile.objects.filter(user_id=user.id).all()
    reg = Registercourses.objects.select_relatected('courses').filter(user_id=user.id)
    context = {'profile':profile, 'reg':reg}        
    return render(request, 'account/dashboard.html', context)

def register(request):
    form = CreateUserForm()    
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()           
            messages.success(request, 'account create successful for ')
            return redirect('profile')
            
    context = {"form":form}
    return render(request, 'account/register.html', context)

def loginpage(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        request.session['username'] = username        
        user = authenticate(request, username=username, password=password)
        if user is not None and user.get_username()!="admin":
            login(request, user)
            return redirect('account/dashboard')
        elif user.get_username()=="admin":
            login(request, user)
            return redirect('user_dashboard')
            
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
            return redirect('account/login')
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

def deleteprofile(request, pk):
    profile = Profile.objects.get(id=pk)
    if request.method == "POST":
        profile.delete()
        return redirect('user_dashboard')
    context = {'item':profile}
    return render(request, 'account/delete.html', context)

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

@login_required(login_url='/account/loginpage')
def course_detail(request, pk):
    profile = Authors.objects.select_related('courses').filter(id=pk)
    context = {"profile":profile}
    return render(request, "account/course_detail.html", context)

def user_dashboard(request):
    count_smm = Registercourses.objects.filter(courses_id=4).count()
    count_gwd = Registercourses.objects.filter(courses_id=5).count()
    count_mc = Registercourses.objects.filter(courses_id=6).count()
    count_bm = Registercourses.objects.filter(courses_id=8).count()
    profile = Profile.objects.select_related('user').all()
    context = {'profile':profile, 'count_smm':count_smm, 'count_gwd':count_gwd, 'count_mc':count_mc, 'count_bm':count_bm}
    return render(request, "account/user_dashboard.html", context)

def contact(request):
    return render(request, 'contactus.html')