from django.db import models

# Create your models here.

#1
class Cite(models.Model):
    libelle = models.CharField(max_length=50)
    lieu = models.CharField(max_length=50)
    #image = models.ImageField()
    description = models.TextField()
    altiude = models.CharField(max_length=50)
    longitude = models.CharField(max_length=50)
    nbr_chmbr_dispo = models.IntegerField()

    def __str__(self):
        return self.libelle

#2
class Categorie(models.Model):
    prix = models.CharField(max_length=50)
    moderne = models.BooleanField(default=False)
    cloturer = models.BooleanField(default=False)
    equipement = models.BooleanField(default=False)
    create_at = models.DateTimeField(auto_now=False,auto_now_add=True)

    def __str__(self):
        return " chambres  de %s  " % self.prix 
        #return f'{self.category.__str__()}'

#3        
class Chambre(models.Model):
    
    libelle = models.CharField(max_length=50)
    #image = mdoels.ImageField( blank=True)
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
