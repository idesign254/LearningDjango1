from django.urls import path
from .import views

app_name = 'articles'

urlpatterns = [
    path('',views.index_view),
    path('articles/',views.home_view),
    path('article-list/',views.article_list),
    path('articles/<int:article_id>/', views.article_detail, name='article_detail'),
]