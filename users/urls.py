# -*- coding:utf-8 -*-

from django.conf.urls import url
from django.views.generic import TemplateView

from . import views

app_name = 'users'

urlpatterns = [
    url('tel_sign_reg', views.tel_sign_reg, name='tel_sign_reg'),
    url('sign_in', views.sign_in, name='sign_in'),
    url('sign_out', views.sign_out, name='sign_out'),
    #url(r'sign_in', TemplateView.as_view(template_name='users/sign_in.html')),

]