from django.contrib import admin
from .models import Article, Commande


class AdminArticle(admin.ModelAdmin):
    list_display = ('nom_art', 'prix', 'categorie', 'qte_stock', 'ref_article')
    search_fields = ('nom_art', )
    list_editable = ('prix', )


class AdminCommande(admin.ModelAdmin):
    list_display = (
        'items',
        'client',
        'nom',
        'prenom',
        'address',
        'ville',
        'pays',
        'phonenumber',
        'total',
        'date_commande',
    )


admin.site.register(Article, AdminArticle)
admin.site.register(Commande, AdminCommande)
