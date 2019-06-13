from django.shortcuts import render,redirect
from .forms import RegisterForm,LoginForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.decorators import login_required
from userprofile.models import UserProfile

# Create your views here.




def register(request):

    form = RegisterForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")

        newUser = User(email=email,username=username)
        newUser.set_password(password)

        newUser.save()
        login(request,newUser)
        messages.success(request,"Başarıyla kayıt oldunuz")

        return redirect("index")
    context = {
        "form":form
    }
    return render(request,"userprofile/register.html",context)


def loginUser(request):
    form = LoginForm(request.POST or None)
    context = {
        "form":form
    }

    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        user = authenticate(username=username,password=password)


        if user is None:
            messages.info(request,"Kullanıcı adınız veya şifreniz hatalı")
            return render(request,"userprofile/login.html",context)
        messages.success(request,"Başarıyla giriş yaptınız")
        login(request,user)

        return redirect("index")
    return render(request,"userprofile/login.html",context)


def logoutUser(request):
    logout(request)
    messages.success(request,"Çıkış yaptınız")
    return redirect("index")


def mypage(request):
   

    return render(request,"userprofile/mypage.html")