# -*- coding:utf-8 -*-

from django.conf.urls import url

from . import views

urlpatterns = [
    # url('employee', views.employee, name='employee'),
    url('insurances/employer/quote', views.employer, name='employer'),
    url('insurances/employee/quote', views.employee, name='employee'),
    url('insurances/team/quote', views.team, name='team'),
    url('insurances/outer/quote', views.outer, name='outer'),
    url('download/', views.download, name='download'),
    # url('team', views.team, name='team'),
    # url('make', views.make, name='make'),
]