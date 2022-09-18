from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render,redirect
from django.template import RequestContext
from django.views import View
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LoginView  
from user_management.forms import LoginForm
# Create your views here.

class Login(View):

    def post(self,request):
        logout(request)
        form = LoginForm(data = request.POST)
        
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate( request , username=username, password=password )

            if user is None: 
                return render ( request , 'user_management/login.html' , { "form" : form } )
            

            login(request, user)
            return redirect("/home/")

        return render(request,'user_management/login.html' , { "form" : LoginForm ,"massage":"worng info"})


    def get(self,request):
        logout(request)
        return render(request,'user_management/login.html' , { "form" : LoginForm })


class Signup(View):
   def post(self,request):
      form = UserCreationForm(request.POST)
      if form.is_valid():
         form.save()
      return render(request,'user_management/login.html' , { "form" : AuthenticationForm })


   def get(self,request):
      form = UserCreationForm()  
      context = {  
        'form':form  
      }      
      return render(request, "user_management/signup.html",context)


class Home(View):
    def get(self,request):
        return render(request, "user_management/home.html")