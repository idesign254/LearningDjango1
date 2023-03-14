from django.shortcuts import render

# Create your views here.
def homepage(request):
    return render(request, 'index.html')

def sign_in(request):
    return render(request, 'sign-in/sign-in.html')

def dashboard(request):
    return render(request, 'dashboard/dashboard.html')
