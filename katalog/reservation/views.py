from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404
from .models import Cite, Chambre
from .forms import ContactForm

#page d'acceuil
def home (request):
    return render (request, 'reservation/home.html')

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





 #les formulaires
 # 
 #    



def contact(request):
    # Construire le formulaire, soit avec les données postées,
    # soit vide si l'utilisateur accède pour la première fois
    # à la page.
    form = ContactForm(request.POST )
    # Nous vérifions que les données envoyées sont valides
    # Cette méthode renvoie False s'il n'y a pas de données 
    # dans le formulaire ou qu'il contient des erreurs.
    if form.is_valid(): 
        # Ici nous pouvons traiter les données du formulaire
        sujet = form.cleaned_data['sujet']
        message = form.cleaned_data['message']
        envoyeur = form.cleaned_data['envoyeur']
        renvoi = form.cleaned_data['renvoi']

        # Nous pourrions ici envoyer l'e-mail grâce aux données 
        # que nous venons de récupérer
        envoi = True
    
    # Quoiqu'il arrive, on affiche la page du formulaire.
    return render(request, 'testes.html', {'form':form})