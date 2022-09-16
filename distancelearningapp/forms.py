from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import *
 
class CreateUserForm(UserCreationForm):
    username = forms.CharField(initial='', widget=forms.TextInput(attrs={"class":"form-control","placeholder":"enter user name..."}))
    email = forms.CharField(initial='',widget=forms.TextInput(attrs={"class":"form-control","placeholder":"email address..."}))
    password1 = forms.CharField(initial='',widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"enter password..."}))
    password2 = forms.CharField(initial='',widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"re-enter password..."}))
    class Meta:
        model = User
        fields =['username', 'email', 'password1', 'password2']

class ProfileForm(ModelForm):    
    class Meta:
        model = Profile
        fields = ('firstname', 'lastname', 'gender','address','contact_phone', 'profile_pic','user')
        widgets = {
            'firstname':forms.TextInput(attrs={'class':'form-control', 'placeholder':'First name'}),
            'lastname':forms.TextInput(attrs={'class':'form-control', 'placeholder':'First name'}),
            'gender':forms.Select(attrs={'class':'form-control'}),
            'address':forms.Textarea(attrs={'class':'form-control','placeholder':'contact address'}),
            'contact_phone':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Phone number'}),
            'profile_pic':forms.FileInput(attrs={'class':'form-control'}),
            'user':forms.Select(attrs={'class':'form-control'})
        }
    
class CourseRegistrationForm(forms.ModelForm):
    class Meta:
        model = Registercourses
        fields = ('name', 'regdate', 'courses', 'user')
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Course'}),
            'regdate':forms.DateInput(attrs={'class':'form-control'}),
            'courses':forms.Select(attrs={'class':'form-control'}),
            'user':forms.Select(attrs={'class':'form-control'})
        }
        