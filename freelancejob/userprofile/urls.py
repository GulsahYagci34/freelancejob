from django.contrib import admin
from django.urls import path
from . import views

app_name ="userprofile"

urlpatterns = [
    path('register/',views.register,name = "register"),
    path('login/',views.loginUser,name="login"),
    path('logout/',views.logoutUser,name="logout"), 
    path('mypage/',views.mypage,name="mypage"),   
]