from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.translation import gettext as _
from django.utils.translation import get_language,activate,gettext
from dashboardapp.models import Voiture,ModuleVoiture,reservation
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
    modules = Voiture.objects.filter(status='libre').values('modulevoiture').annotate(module_count=Count('modulevoiture'))
    cars_list = [{'module': car['modulevoiture'], 'count': car['module_count']} for car in modules]
    json_data = json.dumps({'data': cars_list})
    dats = render_to_string({'modules':json_data})
    return JsonResponse(dats, safe=False)
    return render(request,'rentcarapp/voitures.html',{'modules':modules})
