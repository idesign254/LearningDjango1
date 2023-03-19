from django.contrib import admin

#include urls from other url files
from django.conf.urls import url, include
from django.urls import path, include
from .import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('',views.homepage),
    path('admin/', admin.site.urls),
    
    path('about/',views.about),
    path('services/',views.services),
    path('contact/',views.contact),

    #registers the app name
    url('articles/', include('articles.urls')),
    url('users/', include('users.urls')),
    url('requisition/', include('requisition.urls')),
    url('ecommerce/', include('ecommerce.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)