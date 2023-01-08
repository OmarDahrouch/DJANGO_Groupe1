from django.urls import path
from . import views

app_name = 'article'

urlpatterns = [
    path('', views.home, name="home"),
    path('<int:myid>', views.detail, name="detail"),
]
