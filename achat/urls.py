from django.urls import path
from . import views

app_name = 'achat'

urlpatterns = [
    path('', views.panier, name="panier"),
]
