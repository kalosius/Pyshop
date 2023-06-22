from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def loginpage(request):
    return HttpResponse('loginpage')

def register(request):
    return HttpResponse('register')

def garages(request):
    return HttpResponse('garages')

def mechanics(request):
    return HttpResponse('mechanics')

def vehicles(request):
    return HttpResponse('vehicles')