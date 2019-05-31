from django.shortcuts import render,redirect
from .forms import RegisterForm,LoginForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request,"index.html")


def about(request):
    
    return render(request,"about.html")

def howtowork(request):

    return render(request,"howtowork.html")

@login_required(login_url="userprofile:login")
def register(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")

        newUser = User(email=email,username=username)
        newUser .set_password(password)

        newUser.save()
        login(request,newUser)
        messages.success(request,"Başarı ile Kayıt oldunuz.")

        return redirect("index")
    context = {
        "form":form
    }
     
    
    return render(request,"register.html",context)

@login_required(login_url="userprofile:login")
def loginUser(request):

    form = LoginForm(request.POST or None)
    context = {
        "form" : form
    }

    if form.is_valid():
        username = form.cleaned_data.get("username")
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")

        user =authenticate(email=email,username=username,password=password)

        if user is None:
            messages.info(request,"Email adresiniz veya şifreniz hatalı girildi")
            return render(request,"login.html",context)
        
        messages.success(request,"Başarıyla giriş yaptınız")
        login(request,user)
        
        return redirect("index")
    return render(request,"login.html",context)

    
@login_required(login_url="userprofile:login")
def logoutUser(request):
    logout(request)
    messages.success(request,"Çıkış yaptınız")
    return redirect("index")

