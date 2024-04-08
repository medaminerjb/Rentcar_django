from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Voiture


@login_required
def dashboard(request):
   
    all_car = Voiture.objects.filter()
    context = {
        'cars': all_car
    }        
    return render(request,'dashboardapp/dashboard.html',context)

@login_required
def addcar(request):
    if request.method == 'POST':
            car = request.POST.get('type')
            mod = request.POST.get('mod')
            num = request.POST.get('mat')
            col = request.POST.get('col')
            new_car = Voiture(numeroMat=num,modulecar=mod,couleur=col,type=car)
            new_car.save()
            return redirect('dashboard')
    return render(request,'dashboardapp/caradd.html')
def home(request):
    
    return render(request,'rentcarapp/home.html')
@login_required
def deletecar(request, id):
    car = Voiture.objects.get(id=id)
    car.delete()
    return redirect('dashboard')
@login_required
def getcar(request,id):
    car = Voiture.objects.filter(id=id)
    context ={
          'car':car
     }
    car_ed = Voiture.objects.get(id=id)
    if request.method == 'POST':
            car_ed.type = request.POST.get('type')
            car_ed.modulecar = request.POST.get('mod')
            car_ed.numeroMat = request.POST.get('mat')
            car_ed.couleur = request.POST.get('col')
            car_ed.save()
            return redirect('dashboard')
    return render(request,'dashboardapp/editcar.html',context)

