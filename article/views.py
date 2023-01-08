from django.shortcuts import render, redirect
from .models import Article
from django.core.paginator import Paginator

# Create your views here.


def home(request):
    article_article = Article.objects.all()
    item_name = request.GET.get('item-name')
    if item_name != '' and item_name is not None:
        article_article = Article.objects.filter(nom_art__icontains=item_name)

    paginator = Paginator(article_article, 4)
    page = request.GET.get('page')
    article_article = paginator.get_page(page)
    return render(request, 'article/home.html',
                  {'article_article': article_article})


def detail(request, myid):
    article_article = Article.objects.get(id=myid)
    return render(request, 'article/detail.html', {'article': article_article})


def categorie(request, cat):
    article_article = Article.objects.filter(categorie=cat)
    return render(request, 'article/home.html',
                  {'article_article': article_article})
