from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

from .views import signup
from .views import items
from .views import detail
from .views import edit

from .forms import LoginForm

app_name = 'ecommerce'

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html', authentication_form=LoginForm), name='login'),

    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/delete/', views.delete, name='delete'),
    path('<int:pk>/edit/', views.edit, name='edit'),

    path('SignUp/', views.signup, name='signup'),
    path('items/', views.items, name='items'),
    path('items/', views.detail, name='detail'),
    path('forms/', views.edit, name='edit'),
]
