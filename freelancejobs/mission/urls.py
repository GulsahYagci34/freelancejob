from django.contrib import admin
from django.urls import path
from . import views

app_name ="mission"

urlpatterns = [
      path('createMission/',views.createMission,name="createMission"),
      path('showMission/',views.showMission,name="showMission"),
      path('updateMission/',views.updateMission,name="updateMission"),
]