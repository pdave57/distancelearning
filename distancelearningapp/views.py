from django.shortcuts import render
from .models import Courses
def index(request):
    
    courses = Courses.objects.all()
    return render(request, 'index.html',{'item':courses})

def contact(request):
    return render(request, 'contactus.html')

# Create your views here.
