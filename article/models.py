from django.db import models


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
    email = models.EmailField()
    address = models.CharField(max_length=200)
    ville = models.CharField(max_length=200)
    pays = models.CharField(max_length=300)
    zipcode = models.CharField(max_length=300)
    date_commande = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nom