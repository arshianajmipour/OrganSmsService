"""OrganSmsService URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from user_management.views import Login,Signup
from service_app.views import Home
from django.conf.urls import include
from common_app.views import StateViewSet , CityViewSet, Receiver
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path("admin/", admin.site.urls),
    path("login/",Login.as_view()),
    path("signup",Signup.as_view()),
    path("home/" , login_required(Home.as_view())),
    path('captcha/', include('captcha.urls')),
    path('api/state' , StateViewSet.as_view({'get': 'list'})),
    path('api/state/<int:pk>' , StateViewSet.as_view({'get': 'retrieve'})),
    path('api/city' , CityViewSet.as_view({'get': 'list'})),
    path('api/city/<int:pk>' , CityViewSet.as_view({'get': 'retrieve'})),
    path('/api/service/send', Receiver.as_view())
]
