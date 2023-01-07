from django.shortcuts import render
from .models import Article

# Create your views here.


def index(request):
    return render(request, 'article/index.html')


def home(request):
    article_article = Article.objects.all()
    return render(request, 'article/home.html',
                  {'article_article': article_article})
