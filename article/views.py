from django.shortcuts import render, redirect
from .models import Article, Commande
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

# Create your views here.


def home(request):
    article_article = Article.objects.all()
    item_name = request.GET.get('item-name')
    if item_name != '' and item_name is not None:
        article_article = Article.objects.filter(nom_art__icontains=item_name)

    paginator = Paginator(article_article, 20)
    page = request.GET.get('page')
    article_article = paginator.get_page(page)

    return render(request, 'article/home.html',
                  {'article_article': article_article})


def detail(request, myid):
    article_article = Article.objects.get(id=myid)
    return render(request, 'article/detail.html', {'article': article_article})


@login_required(login_url="/users/login")
def checkout(request):
    if request.method == "POST":
        items = request.POST.get('items')
        total = request.POST.get('total')
        nom = request.POST.get('nom')
        prenom = request.POST.get('prenom')
        phonenumber = request.POST.get('phonenumber')
        address = request.POST.get('address')
        ville = request.POST.get('ville')
        pays = request.POST.get('pays')
        zipcode = request.POST.get('zipcode')
        com = Commande(items=items,
                       total=total,
                       nom=nom,
                       prenom=prenom,
                       address=address,
                       phonenumber=phonenumber,
                       ville=ville,
                       pays=pays,
                       zipcode=zipcode,
                       client=request.user)
        com.save()

    return render(request, 'article/checkout.html')


def categorie(request, cat):
    article_article = Article.objects.filter(categorie=cat)

    paginator = Paginator(article_article, 20)
    page = request.GET.get('page')
    article_article = paginator.get_page(page)

    return render(request, 'article/home.html',
                  {'article_article': article_article})
