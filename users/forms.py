# -*- coding:utf-8 -*-
from __future__ import unicode_literals
from django import forms


class RegisterForm(forms.Form):
    gender = (
        ('male', u"男"),
        ('female', u"女"),
    )
    username = forms.CharField(label=u"用户名", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label=u"密码", max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label=u"确认密码", max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label=u"邮箱地址", widget=forms.EmailInput(attrs={'class': 'form-control'}))
    sex = forms.ChoiceField(label=u'性别', choices=gender)
    #captcha = CaptchaField(label='验证码')


from django.contrib.auth import get_user_model


class LoginForm(forms.ModelForm):
    username = forms.CharField(max_length=11)
    remember = forms.IntegerField(required=False)

    class Meta:
        model = get_user_model()
        fields = ['password']