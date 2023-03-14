from django.urls import path
from .import views

app_name = 'users'

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('sign-in/', views.sign_in, name='sign_in'),
    path('dashboard/', views.dashboard, name='dashboard'),
]
