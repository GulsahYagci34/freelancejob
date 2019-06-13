from django.contrib import admin
from django.urls import path
from . import views

app_name ="mission"

urlpatterns = [
     path('addMission/',views.addMission,name="addmission"),
     path('updateMission/<int:id>/',views.updateMission,name="updatemission"),
     path('deleteMission/<int:id>/',views.deleteMission,name="deletemission"),
     path('myMission/',views.myMission,name="mymission"),
     path('mydetailMission/<int:id>/',views.mydetailMission,name="mydetailmission"),
     path('allMission/',views.allMission,name="allmission"),
     path('alldetailMission/<int:id>/',views.alldetailMission,name="alldetailmission"),
]