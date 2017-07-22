from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from course import views

urlpatterns = [
    url(r'^$',views.course_overview,name='courses'),
    url(r'^view_course/+(?P<course_id>[0-9])+/$',views.view_course,name='view_course'),
]
