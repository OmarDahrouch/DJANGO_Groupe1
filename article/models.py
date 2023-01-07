from django.db import models


class Article(models.Model):
    nom_art = models.CharField(max_length=50, default=None)
    categorie = models.CharField(max_length=50, default=None)
    description = models.CharField(max_length=100)
    ref_article = models.IntegerField()
    prix = models.FloatField()
    qte_stock = models.IntegerField()
    new_image = models.FileField(upload_to="article", null=True, default=None)
