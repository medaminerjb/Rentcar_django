from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Voiture,reservation
from django.http import JsonResponse
import json


def home(request):
    
    return render(request,'rentcarapp/home.html')
def dashboard(request):
    all_cars = Voiture.objects.all()
    cars_list = [{'id': car.id, 'matricule': car.numeroMat} for car in all_cars]
    json_data = json.dumps({'cars': cars_list})

    return JsonResponse(json_data, safe=False)
#####################crud voitures#####################""
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
    return render(request)
@login_required
def getcar(request,id):
    car = Voiture.objects.filter(id=id)
    context ={
          'car':car
     }
    car_ed = Voiture.objects.get(id=id)

    if request.method == 'POST':
            car_ed.modulevoiture = request.POST.get('mod')
            car_ed.numeroMat = request.POST.get('mat')
            car_ed.couleur = request.POST.get('col')
            car_ed.save()
            return redirect('dashboard')
    return render(request,'dashboardapp/editcar.html',context)

@login_required
def deletecar(request, id):
    car = Voiture.objects.get(id=id)
    car.delete()
    return redirect('dashboard')
################reservations pages######################
def reservation_listing(request):
    all_reservations = reservation.objects.filter()
    reservation_list = [{'id': reservation_list.id_reservation, 'matricule': reservation_list.place} for reservation_list in all_reservations]
    json_return = json.dumps({'reservations':reservation_list})
    return JsonResponse(json_return,safe=False)




