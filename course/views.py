from django.shortcuts import render

# Create your views here.
from instructor.models import course


def course_overview(request):
    courses=course.objects.all()
    return render(request,'course/courses.html',{'courses':courses})

def view_course(request,course_id):
   data=course.objects.get(pk=course_id)
   return render(request,'course/view_course.html',{'course':data})
