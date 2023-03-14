from django.shortcuts import render
from .models import Article
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

# Create your views here.
def index_view(request):
    # return render(request, 'index.html')
    articles = Article.objects.all()
    return render(request, 'index.html', {'articles': articles})
def home_view(request):
    return render(request, 'articles/home.html')
    
def article_list(request):
    return render(request, 'article-list/articles_list.html')

def article_detail(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    return render(request, 'single_article/article_detail.html', {'article': article})
