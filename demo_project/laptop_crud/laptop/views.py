from django.shortcuts import render,redirect
from .models import Laptop
from .forms import LaptopForm
from django.contrib.auth.decorators import login_required

# Create your views here.
@ login_required(login_url='loginpage')
def laptop_info(request):
    form=LaptopForm()
    if request.method=="POST":
        form=LaptopForm(request.POST)
        if form.is_valid():
            form.save()

        return redirect('laptop_list')
    template='laptop/addlaptop.html'
    context={'form':form}
    return render(request,template,context)

def show_data(request):
    laptop_obj=Laptop.objects.all()
    template='laptop/show_page.html'
    context={'laptop_obj':laptop_obj}
    return render(request,template,context)

def update_data(request,id):
    laptop_obj=Laptop.objects.get(id=id)
    form=LaptopForm(instance=laptop_obj)
    if request.method=="POST":
        form=LaptopForm(request.POST,instance=laptop_obj)
        if form.is_valid():
            form.save()
            return redirect('laptop_list')
    template='laptop/addlaptop.html'
    context={'form':form}
    return render(request,template,context)


def delete_data(request,id):
    laptop_obj=Laptop.objects.get(id=id)
    laptop_obj.delete()
    laptop_obj.save()
    return redirect('laptop_list')





