# -*- coding: utf-8 -*-
from django.urls import path
from . import views


app_name = 'activrating'

urlpatterns = [path('', views.runusers, name='runusers'),
               path('userprofile/<int:activityId>/', views.userform, name='userform'),
               path('record/', views.recordstat, name='record'),
               path('record/<int:days>/', views.recordstat, name='record'),
               path('userlist/', views.userlist, name='userlist'),
               path('homepage/', views.homepage, name='homepage'),


    ]