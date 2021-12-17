from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

def registerview(request):
    form=UserCreationForm()
    if request.method=="POST":
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('loginpage')
    template='Accountapp/register.html'
    context={'form':form}
    return render(request,template,context)


def loginview(request):
    if request.method=="POST":
        uname=request.POST.get('uname')
        pas=request.POST.get('pass')
        user=authenticate(username=uname,password=pas)
        if user is not None:
            # print(f'username={uname},passowrd={pas}')
            login(request,user)
            return redirect('laptop_add')

        else:
            messages.error(request,'Invalid Credential')

    template='Accountapp/login.html'
    context={}
    return render(request,template,context)

def logoutview(request):
    logout(request)
    return redirect('loginpage')



