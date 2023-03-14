from django.shortcuts import render, get_object_or_404 , redirect
from django.contrib.auth.decorators import login_required
from django.views import View
from django.core.mail import send_mail
from django.conf import settings
from django.db.models import Q
from django.core.files.storage import FileSystemStorage

from .models import Uploads
from .models import School
from .models import Document
from .models import Application
from .forms import ApprovalRequestForm
from .forms import BlogPostForm

from .forms import ApplicationForm

from .forms import UserForm
from .forms import DocumentForm

from .forms import RegistrationForm
from django.contrib.auth.models import User

from django.contrib.auth.views import LogoutView
from .forms import DocumentForm
from django.contrib import messages

from django.utils.text import Truncator

from .forms import SignupForm


# Create your views here.
def view_images(request):
    images = Uploads.objects.all()
    context = {'images': images}
    return render(request, 'View_Document/ViewDocument.html', context)

def upload_image(request):
    if request.method == 'POST':
        image = request.FILES['image']
        image_model = Uploads.objects.create(image=image)
        image_model.save()
    return render(request, 'upload/upload_document.html')


def search_results(request):
    query = request.GET.get('q')
    results = Application.objects.filter(Q(applicant_name__icontains=query) | Q(item__icontains=query))
    return render(request, 'Search/search_results.html', {'results': results, 'query': query})

class ApplicationApprovalView(View):
    def post(self, request, pk):
        application = get_object_or_404(Application, pk=pk)

        # Update the status of the application to reflect the approval.
        application.status = 'approved'
        application.save()

        # Send an email notification to the applicant.
        send_mail(
            'Your application has been approved',
            'Congratulations, your application has been approved!',
            settings.DEFAULT_FROM_EMAIL,
            [application.applicant.email],
            fail_silently=False,
        )

        # Render a confirmation message to the user.
        return render(request, 'Approval/application_approval.html', {'message': message})

def View_Applications(request):
    applications = Application.objects.all()
    return render(request, 'Applications/View_Application.html', {'applications': applications})


def application_detail(request, pk):
    application = get_object_or_404(Application, pk=pk)
    context = {'application': application}
    return render(request, 'Single_Application/View_User_Application.html', context)

def create_post(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST)
        if form.is_valid():
            form.save()
            form = BlogPostForm()  # Reset the form for next submission
            success_message = 'Your post has been submitted successfully!'
    else:
        form = BlogPostForm()
        success_message = ''
    return render(request, 'Blog/blog_post.html', {'form': form, 'success_message': success_message})


def home_view(request):
    return render(request, 'requisition.html')

def Cancel_Approval_Request(request):
    return render(request, 'Cancel_Approval_Request/CancelApprovalRequest.html')

def Document_Approval_Status(request):
    return render(request, 'Document_Approval_Status/Approval.html')

def New_Application(request):
    return render(request, 'New_Application/Application.html')

def Send_Approval_Request(request):
    return render(request, 'Send_Approval_Request/SendApproval.html')

def View_Document(request):
    documents = Document.objects.all()
    return render(request, 'View_Document/ViewDocument.html', {'documents': documents})

def approval_request_view(request):
    form = ApprovalRequestForm()
    context = {'form': form}
    return render(request, 'Send_Approval_Request/SendApproval.html', context)    

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            # return redirect('home')
            success_message = 'Your have registered successfully!'
    else:
        form = RegistrationForm()
        success_message = ''
    return render(request, 'Register/register.html', {'form': form})

# @login_required
def make_application(request):
    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            application = form.save(commit=False)
            application.user = request.user  # Ensure request.user is a valid User instance
            application.save()
            form = ApplicationForm()
            success_message = 'Your application has been submitted successfully!'
    else:
        form = ApplicationForm()
        success_message = ''
    return render(request, 'New_Application/Application.html', {'form': form, 'success_message': success_message})

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid login credentials')
    return render(request, 'Login/login.html')

def upload_document(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('../base.html')  # replace 'home' with the name of your homepage URL
    else:
        form = DocumentForm()
    return render(request, 'New_Document/upload_document.html', {'form': form})

def view_document(request):
    documents = Document.objects.all()
    return render(request, 'View_Document/view_document.html', {'documents': documents})

def document_detail(request, document_id):
    document = get_object_or_404(Document, id=document_id)
    context = {'document': document}
    return render(request, 'Single_Document_View/Single_Document.html', context)


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            return render(request, 'Login/login.html', {'username': username})
    else:
        form = SignupForm()
    return render(request, 'SignUp/signup.html', {'form': form})