from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.template import loader


@login_required(login_url='/users/sign_in')
def edit(request):
    template = loader.get_template('insurances/125.html')
    context = {}
    return HttpResponse(template.render(context, request))


@login_required(login_url='/users/sign_in')
def make(request):
    template = loader.get_template('insurance_items/edit.html')
    context = {}
    return HttpResponse(template.render(context, request))