from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.conf import settings
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
#全局变量 - userinfo
def user_Info(request):
    return {'userInfo': settings.LANGUAGE_CODE,'username':request.session.get("username")}

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

@log_in
def userInfo(request):
    username=request.session.get("username")
    userinfo = user.objects.get(username=username)
    if userinfo.address==None:
        userinfo.address=''
        #return HttpResponse(userinfo.address)
    if request.method != 'POST':
         return render(request,'account/userInfo.html',{'userinfo':userinfo})
    elif request.method == 'POST':
        if request.POST['address']=='':
            return render(request,'account/userInfo.html',{'userinfo':userinfo,'error':'地址不为空'})
        else:
            userinfo.address=request.POST['address']
            userinfo.save()
        return redirect('home')
