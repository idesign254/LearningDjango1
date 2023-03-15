from django.urls import path
from .import views
from .views import create_post
from .views import make_application
from .views import application_detail
from .views import ApplicationApprovalView
from .views import search_results
from .views import login_view
from .views import upload_document
from .views import document_detail

from .views import view_document

from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView
from django.conf.urls.static import static
from django.conf import settings

from django.contrib.auth import views as auth_views

from .forms import LoginForm
from .views import signup


app_name = 'requisition'

urlpatterns = [
    path('Blog/', create_post, name='post_new'),
    path('',views.home_view, name='home'),
    path('Cancel_Approval_Request/',views.Cancel_Approval_Request, name='cancel_approval_request'),
    path('Document_Approval_Status/',views.Document_Approval_Status, name='document_approval_status'),

    path('New_Application/',make_application, name='new_application'),
    path('Send_Approval_Request/',views.Send_Approval_Request, name='send_approval_request'),

    path('View_Document/',views.View_Document,name='view_document'),
    path('Applications/',views.View_Applications,name='view_applications'),

    path('Single_Application/<int:pk>/', views.application_detail, name='application_detail'),

    path('Search/', views.search_results, name='search_results'),
    
    path('Logout/', auth_views.LogoutView.as_view(), name='logout'),

    path('New_Document/', views.upload_document, name='upload_document'),
    path('Single_Document_View/<int:document_id>/', views.document_detail, name='document_detail'),
    path('SignUp/', views.signup, name='signup'),
    path('Login/', auth_views.LoginView.as_view(template_name='Login/login.html', authentication_form=LoginForm), name='login'),
    

]   + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)