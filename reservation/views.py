from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404,redirect
from .models import Cite, Chambre
from .forms import ContactForm,  UserProfileInfoForm
from django.urls import reverse


# Extra Imports for the Login and Logout Capabilities
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required

#page d'acceuil
def home (request):
    all_entries = Cite.objects.all()
    liste_home = {
        "liste" : all_entries
    }
    return render (request, 'reservation/home.html', liste_home)

#adresse pour lister les cites
def cites(request):  
    all_entries = Cite.objects.all()
    liste = {
        "liste" : all_entries
    }
    return render (request, 'reservation/cites.html', liste)

#page pour lister les details des cite
def detail(request, cite_id):
    cite = get_object_or_404(Cite, pk=cite_id)
    chmbr = Chambre.objects.all()
    return render (request, 'reservation/detail.html', { 'citer': cite , 'chmbre' : chmbr})

#page de recherche specifique d'une cite par certains critère
def recherche(request):
    return render(request, 'reservation/recherche.html')

#page pour contacter les admin via email
def nous_contacter(request):
    return render(request, 'reservation/nous_contacter.html')

#petit resumer et presentation des  membre du groupes
def apropos_de_nous(request):
    return render(request, 'reservation/apropos_de_nous.html')

#petit resumer sur la plateformer
def apropos_de_la_plateforme(request):
    return render(request, 'reservation/apropos_de_la_plateforme.html')

def testes(request):
    return render(request,'testes.html')


def update(request, pk):
    obj = get_object_or_404(Cite, pk=pk)
    obj.nbr_chmbr_dispo -= 1
    obj.save() 
    return redirect(reverse('reservation:detail',kwargs={'cite_id':pk}))


 #les formulaires
 # 
 #    

