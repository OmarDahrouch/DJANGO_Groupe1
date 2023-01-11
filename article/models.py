from django.db import models
from django.contrib.auth.models import User


class Article(models.Model):
    nom_art = models.CharField(max_length=50, default=None)
    categorie = models.CharField(max_length=50, default=None)
    description = models.CharField(max_length=5000)
    ref_article = models.IntegerField()
    prix = models.FloatField()
    qte_stock = models.IntegerField()
    new_image = models.ImageField(upload_to="article", default=None)


class Commande(models.Model):
    items = models.CharField(max_length=300)
    total = models.CharField(max_length=200)
    nom = models.CharField(max_length=150)
    prenom = models.CharField(max_length=150, default="")
    phonenumber = models.CharField(max_length=10, null=False, default="")
    address = models.CharField(max_length=200)
    ville = models.CharField(max_length=200)
    pays = models.CharField(max_length=300)
    zipcode = models.CharField(max_length=300)
    date_commande = models.DateTimeField(auto_now=True)
    client = models.ForeignKey(
        User,
        default=None,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.nom