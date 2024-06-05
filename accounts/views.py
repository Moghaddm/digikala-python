from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import login,authenticate

# Create your views here.

def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)
        if user is None:
            context = {
                "error" : "Invalid username or password."
            }
            return HttpResponse(render(request,"accounts/login.html",context))
        return redirect('/products')
    return HttpResponse(render(request,"accounts/login.html",{}))

def logout_view(request):
    return HttpResponse(render(request,"accounts/logout.html",{}))

def register_view(request):
    return HttpResponse(render(request,"accounts/register.html",{}))