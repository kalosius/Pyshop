from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Product


# Create your views here.
def index(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products':products})

def cart(request):
    return HttpResponse('Ooops! The Page is not yet created ' )

def register(request):
    return render(request, 'register.html')

def login(request):
    return render(request, 'login.html')
