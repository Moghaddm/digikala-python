from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm

# Create your views here.

def login_view(request):
    form = AuthenticationForm(request,data = request.POST)
    if form.is_valid():
        user = form.get_user()
        login(request,user)
        return redirect('/products')
    return HttpResponse(render(request,"accounts/login.html",{ "form" : form }))

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('/login')
    return HttpResponse(render(request,"accounts/logout.html",{}))

def register_view(request):
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/login')
    context = {
        "form" : form
    }
    return HttpResponse(render(request,"accounts/register.html",context))