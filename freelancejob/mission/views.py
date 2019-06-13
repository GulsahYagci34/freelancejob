from django.shortcuts import render,redirect,get_object_or_404
from .forms import MissionForm
from .models import Mission,Category,Location
from django.contrib import messages
from django.contrib.auth.decorators import login_required


#index sayfası
def index(request):
    return render(request,"index.html")

#about sayfası
def about(request):
    return render(request,"about.html")

#howtowork sayfası
def howtowork(request):
    return render(request,"howtowork.html")

#görev ekle sayfası
def addMission(request):

    form = MissionForm(request.POST or None,request.FILES or None)
    if form.is_valid():
        mission = form.save()
        mission.createdBy=request.user
        mission.save()
        messages.success(request,"İlanınız yayınlandı.")
        return redirect("index")
    return render(request,"mission/addmission.html",{"form":form})

#görev update sayfası
def updateMission(request,id):
    update = Mission.objects.get(id=id)
    
    form = MissionForm(request.POST or None,request.FILES or None,instance=update)

    if form.is_valid():
        mission = form.save()
        mission.createdBy=request.user
        mission.save()
        
        messages.success(request,"İlanınız güncellendi")
        return redirect("mission:mymission")
    return render(request,"mission/updatemission.html",{"form":form})

#görev kaldır sayfası
def deleteMission(request,id):
    deletemission = Mission.objects.get(id=id)

    deletemission.delete()
    
    messages.success(request,"İlanınız yayından kaldırıldı")
    return redirect("mission:mymission")


#kullanıcının ilanlarının sayfası
def myMission(request):
    #author.id bunu bir dene
    mymissions = Mission.objects.filter(createdBy=request.user.id)
    context = {
        "mymissions":mymissions
    }

    return render(request,"mission/mymission.html",context)


#kullanıcının ilanlarının detaylandırma sayfası
def mydetailMission(request,id):
    detail = Mission.objects.get(id=id)
    
    return render(request,"mission/mydetailmission.html",{"detail":detail})


#ilan havuzu sayfası
def allMission(request):
    
    mymissions = Mission.objects.all()
    context = {
        "mymissions":mymissions
    }

    return render(request,"mission/allmission.html",context)


#ilan havuzundaki ilanların detaylandırma sayfası
def alldetailMission(request,id):
    detail = Mission.objects.get(id=id)
    
    return render(request,"mission/allmissiondetail.html",{"detail":detail})

