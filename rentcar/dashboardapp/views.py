from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Voiture,reservation,ModuleVoiture,marquevehicule,sous_traitance
from .models import agent
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
    modules = ModuleVoiture.objects.filter()
    if request.method == 'POST':
            mod = request.POST.get('module')
            num = request.POST.get('matricule')
            col = request.POST.get('couleur')
            module = ModuleVoiture.objects.get(name_module=mod)
            new_car = Voiture(numeroMat=num,modulevoiture=module,couleur=col)
            new_car.save()
            return redirect('dashboard')
    return render(request,'dashboardapp/caradd.html',{'modules':modules})
@login_required
def getcar(request,id):
    car = Voiture.objects.get(id=id)
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
    return render(request,'dashboardapp/editcar.html',{'car':car})

@login_required
def deletecar(request, id):
    car = Voiture.objects.get(id=id)
    car.delete()
    return redirect('dashboard')
################reservations pages######################
def reservation_listing(request):
    res = reservation.objects.filter()
    #reservation_list = [{'id': reservation_list.id_reservation, 'matricule': reservation_list.place} for reservation_list in all_reservations]
    #json_return = json.dumps({'reservations':reservation_list})
    if request.method =='POST':
        reservatio= request.POST.get('reservation')
        res = reservation.objects.get(id_reservation=reservatio)
        res.status=request.POST.get('statu')
        res.save()
    return render(request,'dashboardapp/reservations.html',{'res':res})
def reservation_statu(request,reserv):
    res = reservation.objects.get(id_reservatio=reserv)
    if request.method == 'POST':
        #if request.POST.get(''):
        if request.method == 'POST':
            res.status = request.POST.get('statu')
            res.save()
    return redirect('dashboard')

########## CRUD modules voitures 
def modulesvoitures(request):
     
     if request.method == 'POST':
        
        name  = request.POST.get('name')
        pui    =  request.POST.get('puissance')
        place =request.POST.get('place')
        res = request.POST.get('reservoir')
        prix = request.POST.get('prix')
        img = request.POST.get('image')
        mar = request.POST.get('marque')
        et = request.POST.get('etat')
        dis = request.POST.get('disponiblite')
        ty = request.POST.get('type')

        mar = marquevehicule.objects.get(name=mar)
        new_module = ModuleVoiture(name_module=name,marque=mar,puissance=pui,nbr_place=place,reservoir=res,prix_neuf=prix,etat=et,desponiblte=dis,type=ty)
        new_module.save()

        return redirect('dashboard')

def edit_modulesvoitures(request,module):
    mar = ModuleVoiture.objects.get(id_module=module)

    if request.method == 'POST':
        mar.name_module = request.POST.get('name')
        mar.puissance    =  request.POST.get('puissance')
        mar.nbr_place =request.POST.get('place')
        mar.reservoir = request.POST.get('reservoir')
        mar.prix_neuf = request.POST.get('prix')
        mar.image = request.POST.get('image')
        mar.marque = request.POST.get('marque')
        mar.etat = request.POST.get('etat')
        mar.desponiblte = request.POST.get('disponiblite')
        mar.type = request.POST.get('type')

        mar.save()

        return redirect('dashboard')
@login_required
def deletemodule(request, module):
    mar = ModuleVoiture.objects.get(id_module=module)
    mar.delete()
    return redirect('dashboard')
################Crud marques
def marque_listing(request):
    marques = marquevehicule.objects.all()

    return render(request,'dashboardapp/marques',{'marque':marques})

def addmarque(request):
    if request.method == 'POST':
        namemar= request.POST.get('name')
        mar= marquevehicule(name=namemar)
        mar.save()
    return redirect('dashboard')
def editmarque(request,marque):
    mar = marquevehicule.objects.get(id_marque=marque)
    if request.method == 'POST':
        mar.name=request.POST.get('name')
        mar.save()
    return redirect('dashboardapp')  
def deletemarque(request,marque):
    mar = marquevehicule.objects.get(id_marque=marque)
    mar.delete()
    return redirect('dashboard')
#########################Sous Traitence 
def add_soustraitence(request):
        
    if request.method == 'POST':    
        taux_ech = request.POST.get('')        
        number_ech = request.POST.get('')
        number_echance_pa = request.POST.get('')
        ava = request.POST.get('')
        date_pai = request.POST.get('')
        date_deb = request.POST.get('')
        date_fi = request.POST.get('')
        voit = request.POST.get('')
        agen = request.POST.get('')
        obj = sous_traitance(taux_echeance=taux_ech,number_echeance=number_ech
                             ,number_echance_paier=number_echance_pa,avance=ava
                             ,date_paiment=date_pai,date_debut=date_deb,date_fin=date_fi
                             ,voiture=voit,agent=agen)
        obj.save()


def edit_soustraitance(request,sous):
    so = sous_traitance.objects.get(id_sous_traitance=sous)
    so.taux_echeance = request.POST.get('')        
    so.number_echeance = request.POST.get('')
    so.number_echance_paier = request.POST.get('')
    so.avance = request.POST.get('')
    so.date_paiment = request.POST.get('')
    so.date_debut = request.POST.get('')
    so.date_fin = request.POST.get('')
    so.voiture = request.POST.get('')
    so.agent = request.POST.get('')
    so.save()
    return redirect('dashboard')

def soustraitence_listing(request):
    sous = sous_traitance.objects.all()


    return render(request,'dashboardapp/soustraitance.html',{'sous':sous})

def his_st(request,soustraitence):
    so = sous_traitance.objects.get(id_sous_traitance=soustraitence)

    return render(request,'dashboard/historique.html',{'sous':so})
##################agent part admin ############
def add_agent(request):
    if request.method == 'POST':

        if request.POST.get('addagent'):
            namea = request.POST.get('')
            emaila = request.POST.get('')
            numerotela = request.POST.get('')
            usera = request.POST.get('user')
            userf = User.objects.get(user=usera)
            data = agent(name=namea,email=emaila,numerotel=numerotela,user=userf)
            data.save()
    return redirect('dashboard')

def delete_agent(request,age):
    agent_data = agent.objects.get(name=age)
    agent_data.delete()
    return redirect('dashboardapp')
##############agent part agent 
#def voitures_listing(request):

        


        


     








