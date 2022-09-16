from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Courses(models.Model):
    courseTitle = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    course_pic = models.FileField(blank=True, null=True, upload_to="upload/")
    start_date = models.DateField()
    duration = models.CharField(max_length=50)
    def __str__(self):
        return self.courseTitle    
    
class Authors(models.Model):
    author = models.CharField(max_length=50)
    author_pic = models.FileField(blank=True, null=True, upload_to="upload/")
    price = models.DecimalField(decimal_places=2, max_digits=5)
    courses = models.ForeignKey(Courses, on_delete=models.CASCADE)
    def __str__(self):
        return self.author
    

class Registercourses(models.Model):
    #users = models.ForeignKey(User)    
    name = models.CharField(max_length=200)    
    regdate = models.DateField()
    courses = models.ForeignKey(Courses, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.name
    

class Contactus(models.Model):
    fullname = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    message = models.CharField(max_length=500)
    def __str__(self):
        return self.fullname
    
    
class Reviews(models.Model):        
    review = models.CharField(max_length=500)
    rating = models.CharField(max_length=5)
    user = models.ForeignKey(User, default="",on_delete=models.CASCADE)
    def __str__(self):
        return self.review
    
    
class Profile(models.Model):
    GENDER = (
        ('M', 'MALE'),
        ('F', 'FEMALE')
    )    
    
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    gender = models.CharField(max_length=5, choices=GENDER)
    address = models.CharField(max_length=100)
    contact_phone = models.CharField(max_length=50)
    profile_pic = models.ImageField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.firstname
    

