from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # path('contact', views.contact, name ='contact'),
    path('', views.index, name='index'),
    path('account/register', views.register, name='account/register'),
    path('account/login', views.loginpage, name='account/login'),
    path('account/logout', views.logoutUser, name='logout'),
    path('account/dashboard', views.dashboard, name='account/dashboard'),
    path('account/profile', views.createprofile, name='account/profile'),
    path('updateprofile/<str:pk>', views.editprofile, name='updateprofile'),
    path('account/course_details/<str:pk>/', views.course_detail, name='account/course_details'),
    path('course_registration', views.course_registration, name="course_registration")
    
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)