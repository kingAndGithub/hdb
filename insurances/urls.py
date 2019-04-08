# -*- coding:utf-8 -*-

from django.conf.urls import url

from . import views

urlpatterns = [
    url('employee/', views.employee, name='employee'),
    url('employer/', views.employer, name='employer'),
    url('outer', views.outer, name='outer'),
    url('team/', views.team, name='team'),
    url('^$', views.index, name='index'),
]