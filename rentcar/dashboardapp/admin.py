from django.contrib import admin
from .models import Client, Voiture, ModuleVoiture, agent
from .models import reservation, sous_traitance, historique_st,marquevehicule

# Trip and it's Meta
class ClientAdmin(admin.ModelAdmin):
    model = Client
class marquevehiculeadmin(admin.ModelAdmin):
    model = marquevehicule
class modulevehiculeAdmin(admin.ModelAdmin):
    model = ModuleVoiture
class VoitureAdmin(admin.ModelAdmin):
    model = Voiture

class agentAdmin(admin.ModelAdmin):
    model = agent

class reservationAdmin(admin.ModelAdmin):
    model = reservation

class sous_traitanceadmin(admin.ModelAdmin):
    model = sous_traitance

class historique_stadmin(admin.ModelAdmin):
    model = historique_st



admin.site.register(Voiture,VoitureAdmin)
admin.site.register(ModuleVoiture,modulevehiculeAdmin)
admin.site.register(marquevehicule,marquevehiculeadmin)
admin.site.register(Client,ClientAdmin)
admin.site.register(agent,agentAdmin)
admin.site.register(reservation,reservationAdmin)
admin.site.register(sous_traitance,sous_traitanceadmin)
admin.site.register(historique_st,historique_stadmin)


