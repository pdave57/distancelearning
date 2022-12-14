"""distancelearning URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('distancelearningapp.urls')),
    path('admin/', admin.site.urls),
    path('account/register', include('distancelearningapp.urls')),
    path('account/login', include('distancelearningapp.urls')),
    path('logout', include('distancelearningapp.urls')),
    path('account/dashboard', include('distancelearningapp.urls')),
    path('profile', include('distancelearningapp.urls')),
    path('updateprofile/<str:pk>/', include('distancelearningapp.urls')),
    path('delete_profile/<str:pk>/', include('distancelearningapp.urls')),        
    path('account/course_details/<str:pk>/', include("distancelearningapp.urls")),
    path('course_registration', include('distancelearningapp.urls'))
    # path('contact', include('distancelearningapp.urls')),
]
