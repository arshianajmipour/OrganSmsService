from django import forms
from django.contrib.auth.models import User
from captcha.fields import CaptchaField
from django.contrib.auth.forms import AuthenticationForm


class LoginForm(AuthenticationForm):  
    captcha = CaptchaField()
    # class Meta:  
    #     model = User
    #     fields = ['username', 'password']
    #     widgets = {
    #         'password': forms.PasswordInput() 
    #     }
