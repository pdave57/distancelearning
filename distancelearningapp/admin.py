from django.contrib import admin
from .models import Courses, CourseAuthors

# Register your models here.
admin.site.register(Courses)
admin.site.register(CourseAuthors)
