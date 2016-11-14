# coding: utf-8
from django.shortcuts import render, redirect
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.models import User
from myblog.models import Blogger

# Create your views here.


def registration(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        if username and password and email:
            user = User.objects.create_superuser(
                username=username,
                password=password,
                email=email
            )
            Blogger.objects.create(
                User=user,
                id=user.id,
                Nickname=username
            )
            login(request, user)
            return redirect('/blog')
        else:
            pass
    else:
        pass
    return render(request, 'index/registration.html')


def log_in(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            user = User.objects.get(username=username)
            if user.blogger.Status:
                login(request, user)
                return redirect('/blog')
            else:
                return render(request, 'myblog/missing_blogger.html')
        else:
            pass          # 传递参数，提示 #######################################
    else:
        pass
    return render(request, 'index/login.html')


def log_out(request):
    logout(request)
    return redirect('/blog')
