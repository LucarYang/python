from django.shortcuts import render, redirect
import json

from .models import user

# Create your views here.

#身份认证装饰器
def log_in(func):
    def wrapper(request,*args,**kwargs):
        try:
            request.session.get("username",False)
            if not request.session.get("username"):
                return redirect('login')
        except KeyError:
            return redirect('login')
        return  func(request,*args, **kwargs)
    return wrapper


@log_in
def home(request):
    try:
        name=request.session.get("username")
        userinfo = user.objects.get(username=name)
        return render(request, 'home.html',{'user':userinfo})
    except Exception as e:
        return render(request,'login.html',{'error':str(e)}) 

def signup(request):
    if request.method == 'POST':
        if request.POST['password']==request.POST['password1']:
            user.objects.create(username=request.POST['username'],email=request.POST['email'],password=request.POST['password1'])
            return redirect('home')
    return render(request, 'signup.html')

def login(request):
    if request.method == 'POST':
        if request.method == 'POST':
            if user.objects.filter(username=request.POST['username'],password=request.POST['password']).count():
                request.session["username"] = request.POST['username']
                return redirect('home')
            elif user.objects.filter(email=request.POST['username'],password=request.POST['password']).count():
                userinfo = user.objects.get(email=request.POST['username'])
                request.session["username"] =userinfo.username
                return redirect('home')
            else:
                return render(request,'login.html',{'error':'登录名或密码不正确！'}) 
    return render(request,'login.html')

def logout(request):
    del request.session['username']
    return redirect('home')

def userInfo(request):
    return render(request,'account/userInfo.html')
