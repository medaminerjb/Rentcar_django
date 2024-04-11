from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.translation import gettext as _
from django.utils.translation import get_language,activate,gettext
from dashboardapp.models import Voiture,ModuleVoiture,reservation,Prices
from django.http import JsonResponse
import json
from django.db.models import Count
from django.template.loader import render_to_string



def signupView(request):

    return render(request,'rentcarapp/signup.html',{})

def loginView(request):
    if request.user.is_authenticated:
       return redirect('home')
    if request.method == 'POST':
        if 'signup' in request.POST:
            username = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('password')
            new_user = User.objects.create_user(username=username, email=email, password=password)
            new_user.save()
            return redirect('home')
    
        if 'login' in request.POST:
            username = request.POST.get('username')
            password = request.POST.get('password')

            validate_user = authenticate(username=username, password=password)
            if validate_user is not None:
                login(request, validate_user)
                return redirect('dashboard')
            else:
                return redirect('login')

    return render(request,'rentcarapp/login.html',{})
@login_required
def dashboard(request):
    voitures = Voiture.objects.filter()
    return render(request,'dashboardapp/dashboard.html',{'voitures':voitures})
@login_required
def LogoutView(request):
    logout(request)
    return redirect('login')
def home(request):
    modules = ModuleVoiture.objects.filter()
    return render(request,'rentcarapp/home.html',{'modules':modules})

def voitures_listing(request):
    modules = Voiture.objects.values('modulevoiture').annotate(module_count=Count('modulevoiture'))

    voitures = ModuleVoiture.objects.filter()
    prices = Prices.objects.filter()
    for i in voitures :
        for j in modules :
            if i.id_module == j['modulevoiture']:
                i.module_count = j['module_count']
        for t in prices :
            if t.module == i :
                i.price = t.price

    return render(request, 'rentcarapp/voitures.html', {'modules': voitures})
########search form ########
from django.db.models import Q
from datetime import date

def search_listing(request):

    if request.method == 'POST':
        if request.POST.get == 'voituresearch':

            modulev = request.POST.get('')
            datesor = request.POST.get('')
            dateret = request.POST.get('')



# Get all cars
        all_cars = Voiture.objects.all()

        available_cars = []

        for car in all_cars:
    # Query reservations for this car that overlap with the given date range
            reservations_overlap = reservation.objects.filter(

                Q(start_date__lte=datesor, end_date__gte=datesor) |
                Q(start_date__lte=dateret, end_date__gte=dateret) |
                Q(start_date__gte=datesor, end_date__lte=dateret)
                )
###fixes
    # If there are no overlapping reservations, add the car to available_cars
        if not reservations_overlap.exists():
            available_cars.append(car)
            print("Available cars:")
        for car in available_cars:
            print(f"{car.module} {car.model}")
            return render()
 



