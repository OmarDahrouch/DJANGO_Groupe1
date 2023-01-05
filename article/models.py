from django.db import models


class Article(models.Model):
    description = models.CharField(max_length=100)
    ref_article = models.IntegerField()
    prix = models.FloatField()
    qte_stock = models.IntegerField()
