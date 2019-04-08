# -*- coding:utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.
from django.template import loader


def outer(request):
    path = request.path
    page_num = path.split('/')[-1]
    if page_num.isalnum():
        html = "insurances/{}.html".format(page_num)
    else:
        html = "insurances/121.html"
    template = loader.get_template(html)
    context = {}
    return HttpResponse(template.render(context, request))


def team(request):
    path = request.path
    page_num = path.split('/')[-1]
    if page_num.isalnum():
        html = "insurances/{}.html".format(page_num)
    else:
        html = "insurances/7.html"
    template = loader.get_template(html)
    context = {}
    return HttpResponse(template.render(context, request))


def employer(request):
    path = request.path
    page_num = path.split('/')[-1]
    if page_num.isalnum():
        html = "insurances/{}.html".format(page_num)
    else:
        html = "insurances/125.html"
    template = loader.get_template(html)
    context = {}
    return HttpResponse(template.render(context, request))


@login_required(login_url='/users/sign_in')
def index(request):
    template = loader.get_template('blogapp/index.html')
    context = {}
    return HttpResponse(template.render(context, request))


def employee(request):

    path = request.path
    page_num = path.split('/')[-1]
    if page_num.isalnum():
        html = "insurances/{}.html".format(page_num)
    else:
        html = "insurances/129.html"
    template = loader.get_template(html)
    context = {}
    return HttpResponse(template.render(context, request))
