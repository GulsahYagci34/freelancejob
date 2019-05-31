from django.shortcuts import render,redirect,get_object_or_404,reverse
from .forms import MissionForm
from .models import Mission,Location,Category
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required(login_url="userprofile:login")
def createMission(request):
   
    form=MissionForm(request.POST or None,request.FILES or None)

    if form.is_valid():
        mission= form.save(commit=False)

        mission.author=request.user
        mission.save()
        messages.success(request,"Görevi başarıyla yayınladı")
        return redirect("index")
    
    return render(request,"createmission.html",{"form":form})

@login_required(login_url="userprofile:login")
def showMission(request):
    return render(request,"usermission.html")
    
@login_required(login_url="userprofile:login")
def updateMission(request):
    return render(request,"updatemission.html")  

    
@login_required(login_url="userprofile:login")
def deleteMission(request,id):

    messages.success(request,"İlan silindi")
    return redirect("index")


