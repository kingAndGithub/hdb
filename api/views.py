# -*- coding:utf-8 -*-
import json
import os

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render


# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from api.const import PLAN_MAP, MONTH_MAP, LEVEL_MAP, AGE_MAP
from mysite.settings import BASE_DIR


@csrf_exempt
def employer(request):

    aspector = json.loads(request.body)
    age = aspector.get("age", 0)
    level = aspector.get("level", 0)
    month = aspector.get("month", 0)
    plan = aspector.get("plan", 0)
    base = PLAN_MAP[plan]
    base_on_month = MONTH_MAP[month] * base
    base_on_level = LEVEL_MAP[level] * base_on_month
    base_on_age = AGE_MAP[age] * base_on_level
    price = base_on_age
    return JsonResponse({"code": '0000', "data": {"price": price}, "message": price})


@csrf_exempt
def employee(request):
    PLAN_MAP = {
        "129": 9,
        "130": 18.6,
        "131": 28.6,
        "132": 45.8,
    }
    aspector = json.loads(request.body)
    age = aspector.get("age", 0)
    level = aspector.get("level", 0)
    month = aspector.get("month", 0)
    plan = aspector.get("plan", 0)
    base = PLAN_MAP[plan]
    base_on_month = MONTH_MAP[month] * base
    base_on_level = LEVEL_MAP[level] * base_on_month
    base_on_age = AGE_MAP[age] * base_on_level
    price = base_on_age
    return JsonResponse({"code": '0000', "data": {"price": price}, "message": price})


@csrf_exempt
def team(request):
    AGE_MAP = {
        "46": {"1": 2645, "2": 2976},
        "51": {"1": 3555, "2": 4000},
        "56": {"1": 4993, "2": 4617},
        "61": {"1": 6614, "2": 7441},
    }
    aspector = json.loads(request.body)
    age = aspector.get("age", 0)
    level = aspector.get("level", 0)
    if AGE_MAP.get(age):
        price = AGE_MAP.get(age)[level]
    else:
        price = 2400
    return JsonResponse({"code": '0000', "data": {"price": price}, "message": price})


@csrf_exempt
def outer(request):
    ALL_MAP = {
        "121":{
            "base": 10,
            "DAY_MAP": {
                "1": 10,
                "2": 20,
                "4": 30,
                "6": 50,
                "11": 90,
                "16": 130,
                "21": 170,
            }
        },
        "122": {
            "base": 20,
            "DAY_MAP": {
                "1": 20,
                "2": 30,
                "4": 50,
                "6": 80,
                "11": 140,
                "16": 200,
                "21": 260,
            }
        },
        "123": {
            "base": 30,
            "DAY_MAP": {
                "1": 30,
                "2": 45,
                "4": 75,
                "6": 120,
                "11": 195,
                "16": 270,
                "21": 345,
            }
        },
        "124": {
            "base": 50,
            "DAY_MAP": {
                "1": 50,
                "2": 75,
                "4": 125,
                "6": 200,
                "11": 325,
                "16": 450,
                "21": 575,
            }
        },

    }
    aspector = json.loads(request.body)
    day = aspector.get("day", 0)
    plan = aspector.get("plan", 0)
    price = 0
    if ALL_MAP.get(plan):
        price = ALL_MAP.get(plan)["DAY_MAP"][day]
    return JsonResponse({"code": '0000', "data": {"price": price}, "message": price})


@csrf_exempt
def download(request):
    path = request.path
    pdf_file = path.split('/')[-1]
    file_name = "./static/files/" + pdf_file
    lj = os.path.join(BASE_DIR, 'static')
    opened_file = open(file_name, 'rb')
    response = HttpResponse(opened_file)
    response['Content-Type'] = 'application/octet-stream'  # 设置头信息，告诉浏览器这是个文件
    response['Content-Disposition'] = 'attachment;filename="%s"' % file_name
    return response

