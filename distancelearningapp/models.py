from django.db import models

# Create your models here.
class Courses(models.Model):
    courseTitle = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    course_pic_url = models.FileField(upload_to='images/uploadcimg/')
    start_date = models.DateField()
    duration = models.CharField(max_length=50)
    def __str__(self):
        return self.courseTitle
       
    
    
class Authors(models.Model):
    author = models.CharField(max_length=50)
    author_pic_url = models.FileField(upload_to='images/uploadaimg/')
    price = models.DecimalField(decimal_places=2, max_digits=5)
    courses = models.ForeignKey(Courses, on_delete=models.CASCADE)
    def __str__(self):
        return self.author
    

class CourseReg(models.Model):
    userId = models.IntegerField()    
    creg = models.CharField(max_length=100)    
    regdate = models.DateField()
    courses = models.ForeignKey(Courses, on_delete=models.CASCADE)
    def __str__(self):
        return self.creg
    

class Contactus(models.Model):
    fullname = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    message = models.CharField(max_length=500)
    def __str__(self):
        return self.fullname
    
    
class Studentreviews(models.Model):
    profileId = models.IntegerField()
    course = models.CharField(max_length=100)
    review = models.CharField(max_length=500)
    rating = models.CharField(max_length=5)
    def __str__(self):
        return self.course
    
    
class Studentprofile(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    gender = models.CharField(max_length=5)
    address = models.CharField(max_length=100)
    contact_phone = models.CharField(max_length=50)
    def __str__(self):
        return self.firstname
    