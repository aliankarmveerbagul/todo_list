from django.shortcuts import render,redirect
from .task import *
from .models import *


def home(request):
    read = to_data.objects.all()
    return render(request,'home.html',{'read':read})

def create(request):
    if request.method == "POST":
        u = taskform(request.POST)
        u.save()
        return redirect('app_todo:home')
    create = taskform()
    return render(request, 'create.html', {'create':create})



def update(request,id):
    abc = to_data.objects.get(s_no=id)
    print(abc)
    if request.method == "POST":
        u = taskform(request.POST, instance=abc)
        u.save()
        return redirect('app_todo:home')
    else:
        print("HELLO")

    read = taskform(instance=abc)
    return render(request,'update.html',{'read':read,'abc':abc})



def delete(request,id):
    dell = to_data.objects.get(s_no=id)
    dell.delete()
    return redirect('/')