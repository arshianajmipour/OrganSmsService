from django.shortcuts import render
from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render,redirect
from django.template import RequestContext
from django.views import View
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
# Create your views here.
class Home(View):
   def get(self,request):
      
      if request.user.is_authenticated:
         return render(request, "service_app/home.html", {})

      else:
         return redirect("/login/")