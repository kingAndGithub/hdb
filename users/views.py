# -*- coding:utf-8 -*-
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render, redirect
# Create your views here.
from django.template import loader

from django.contrib import auth
from django.http import Http404, HttpResponse, HttpResponseRedirect
import json
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.views.decorators.cache import never_cache
from django.views.decorators.http import require_POST

from users import models
from users.forms import LoginForm
from django.contrib.auth.models import User



@csrf_exempt
def tel_sign_reg(request):
    template = loader.get_template('users/tel_sign_reg.html')
    context = {}
    if request.method == 'POST':
        data = request.POST
        user_name = data.get('username', '')
        pass_word = data.get('password', '')
        User.objects.create_user(username=user_name, password=pass_word)

        return render(request, 'users/sign_in.html', {})
    elif request.method == 'GET':
        return render(request, 'users/tel_sign_reg.html', {})


@csrf_exempt
def sign_in(request):
    template = loader.get_template('users/sign_in.html')
    context = {}
    """
            用户登录方法
        """
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if request.session.get('is_login', None):
            next_url = request.GET.get('next')
            if next_url:
                # 重定向到设置好的登录页面
                return redirect(next_url)
            else:
                return redirect("/")

        username = form.data.get('username')
        password = form.data.get('password')
        remember = form.data.get('remember')

        user = authenticate(username=username, password=password)
        message = ""
        if user is not None:
            # 判断用户是否被冰冻
            if user.is_active:
                login(request, user)
                # 判断是否记住密码
                request.session['is_login'] = True
                request.session['user_id'] = user.id
                request.session['user_name'] = user.username
                if remember:
                    # 设置为None，则表示使用全局的过期时间
                    request.session.set_expiry(None)
                else:
                    # 设置浏览器关闭之后就过期
                    request.session.set_expiry(0)
                    # 这里的设置网址有next后缀的处理方法
                path = request.META['HTTP_REFERER']
                if "next" in path:
                    next_url = path.split('next=')[1]
                    if next_url:
                        # 重定向到设置好的登录页面
                        return redirect(next_url)
                    else:
                        return redirect("/")
            else:
                return redirect("/")
        else:
            message = u"用户名或密码错误！"

        return render(request, 'users/sign_in.html', {"msg": message})

    elif request.method == 'GET':
        return render(request, 'users/sign_in.html', {})

    #return HttpResponse(template.render(context, request))


@csrf_exempt
def sign_out(request):
    if not request.session.get('is_login', None):
        # 如果本来就未登录，也就没有登出一说
        return redirect("/")
    request.session.flush()
    # 或者使用下面的方法
    # del request.session['is_login']
    # del request.session['user_id']
    # del request.session['user_name']
    return redirect("/")