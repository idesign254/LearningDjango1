from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    #return HttpResponse('homepage')
    return render(request, "homepage.html")

def about(request):
    #return HttpResponse('about')
    return render(request, "about.html")

def services(request):
    return render(request, "services.html")

def contact(request):
    #return HttpResponse('about')
    return render(request, "contact.html")