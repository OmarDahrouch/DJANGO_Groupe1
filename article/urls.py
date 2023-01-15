from django.urls import path
from . import views

app_name = 'article'

urlpatterns = [
    path('', views.home, name="home"),
    path('<int:myid>', views.detail, name="detail"),
    path('checkout/', views.checkout, name="checkout"),
    path('valide/', views.valide_view, name="valide"),
    path('article/<str:cat>', views.categorie, name="cat")
]
