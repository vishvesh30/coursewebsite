from django.contrib import admin
from .models import instructor, course, enrolldata, coursecontent

# Register your models here.

admin.site.register(course)
admin.site.register(enrolldata)
admin.site.register(coursecontent)