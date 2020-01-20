from django.db import models
from django.contrib.auth.models import User

# Create your models here.

#1
class Cite(models.Model):
    libelle = models.CharField(max_length=50)
    lieu = models.CharField(max_length=50)
    image = models.ImageField(default='20190805_112608jpg' ,null=True,blank=True)
    description = models.TextField()
    nbr_chmbr_dispo = models.IntegerField()
    prix = models.IntegerField()
    contact = models.IntegerField(default=694216755)

    def __str__(self):
        return self.libelle

#2
class Categorie(models.Model):
    prix = models.CharField(max_length=50)
    moderne = models.BooleanField(default=False)
    cloturer = models.BooleanField(default=False)
    equipement = models.BooleanField(default=False)
    create_at = models.DateTimeField(auto_now=False,auto_now_add=True)
    caution = models.prix = models.CharField(default="10000", max_length=50)

    def __str__(self):
        return " chambres  de %s  " % self.prix 
        #return f'{self.category.__str__()}'

#3        
class Chambre(models.Model):
    
    libelle = models.CharField(max_length=50)
    image = models.ImageField(default='20190805_112608jpg' ,null=True,blank=True)
    description = models.TextField()
    cite     = models.ForeignKey(Cite,on_delete=models.CASCADE)
    categorie = models.ForeignKey(Categorie,on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now=False,auto_now_add=True)

    def __str__(self):
        return self.libelle




#4
class client(models.Model):
     nom = models.CharField(max_length=50)
     prenom = models.CharField(max_length=50)
     date_naiss = models.DateField()
     lieu = models.CharField(max_length=50)
     sexe = models.CharField(max_length=50)
     tel = models.CharField(max_length=10)
     email = models.CharField(max_length=50)
     photo = models.CharField(max_length=50)

     def __str__(self):
        return self.nom

#5
class Commentaire(models.Model):    
    message   = models.TextField()
    chambre   = models.ForeignKey(Chambre,on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now=False,auto_now_add=True)
    IdClient = models.ForeignKey(client ,on_delete=models.CASCADE)

    def __str__(self):
        return " la %s " % self.message




#6
class reserv(models.Model):
    dateDebut = models.DateField()
    dateFin   = models.DateField()
    idUtilisateur = models.ForeignKey(client, on_delete=models.CASCADE)
    idChambre = models.ForeignKey(Chambre, on_delete= models.CASCADE)
    actif = models.BooleanField(default=True)

    def __str__(self):
        #self.msg = " reservations  de "
        return "Réservation de %s " % self.idUtilisateur

class UserProfileInfo(models.Model):

    # Create relationship (don't inherit from User!)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # Add any additional attributes you want
    portfolio_site = models.URLField(blank=True)
    # pip install pillow to use this!
    # Optional: pip install pillow --global-option=”build_ext” --global-option=”--disable-jpeg”
    profile_pic = models.ImageField(upload_to='profile_pics',blank=True)

    def __str__(self):
        # Built-in attribute of django.contrib.auth.models.User !
        return self.user.username
