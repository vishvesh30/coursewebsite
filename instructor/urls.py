from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from instructor import views

urlpatterns = [
    url(r'^login/$',views.login,name='instructor_login'),
    url(r'^panel/$',views.instructor_panel,name='instructor_panel'),
    url(r'^createcourse/$',views.create_course,name='create_course'),
    url(r'^managecourse/$',views.managecourse,name='managecourse'),
    url(r'^managecourse/+(?P<course_id>[0-9])+/$',views.edit_course,name='editcourse'),
    url(r'^logout/$',views.logout,name='instructor_logout'),
    url(r'^createcourse1/$', views.create_course1, name='createcourse1'),
]
