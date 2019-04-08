# -*- coding:utf-8 -*-

from django.conf.urls import url

from . import views

urlpatterns = [
    url('(?P<pk>(\d+))/edit', views.edit, name='edit'),
    # url('employer/', views.employer, name='employer'),
    # url('outer', views.outer, name='outer'),
    # url('team/', views.team, name='team'),
    url('make', views.make, name='make'),
]