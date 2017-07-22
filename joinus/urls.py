from django.conf.urls import url, include
from django.contrib import admin

from joinus import views

urlpatterns = [

    url(r'^register/$', views.register,name='register'),
    url(r'^login/$',views.login,name='login'),
    url(r'^signout/$',views.signout,name='login'),
    url(r'^demo/$',views.demo,name='demo'),
]
