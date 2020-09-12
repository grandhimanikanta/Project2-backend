"""Hackthon URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path,include
from rest_framework.authtoken.views import obtain_auth_token
from django.contrib.auth.models import User
from rest_framework import routers
from Hackapp import views
from Hackapp.views import UserLoginAPIView, UserLogoutAPIView, UserVerifyLoginAPIView,RoleInfo, RoleEdit,isrecruier,listofusers

app_name='users'

router=routers.DefaultRouter()
router.register('user',views.UserViewSet,basename='user-api')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/login/', UserLoginAPIView.as_view(), name="login"),
    path('users/logout/', UserLogoutAPIView.as_view(),name="logout"),
    path('users/verify_login/', UserVerifyLoginAPIView.as_view(),name="logout"),
    path('api/',include(router.urls)),
    path('roleinfo/',RoleInfo.as_view(),name='roleinfo'),
    path('editrole/',RoleEdit.as_view(),name='editrole'),
    path('isrecruiter/',isrecruier.as_view(),name='isrecruiter'),
    path('listofusers/',listofusers.as_view(),name='listofusers'),
]
