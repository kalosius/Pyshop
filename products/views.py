from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Product, Registration
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
# Create your views here.



def index(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products':products})


def cart(request):
    products = Product.objects.all()
    return render(request, 'cart.html', {'products':products} )

def register(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if request.method == 'POST':
            name = request.POST['name']  
            email = request.POST['email']
            password = request.POST['password'] 
            phone = request.POST['phone']
            job = request.POST['job']

            myuser = User.objects.create_user(name, email, password)
            myuser.save()
            messages.info(request, 'Account Created Successfully!')
            return redirect('login')
    return render(request, 'register.html', {'form':form})

def loginpage(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.info(request, 'Email or password is incorrect')
            return redirect('loginpage.html')
    return render(request, 'loginpage.html')



def services(request):
    return render(request, 'services.html')


def data(request):
    regview = Registration.objects.all()
    return render(request, 'data.html', {'regview':regview})

@login_required
def logout(request):
    return render(request, logout)
