from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.shortcuts import redirect

def home(request):
    if request.user.is_authenticated:
        return render(request, 'home.html')
    else:
        return redirect(reverse('login'))

def login_user(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    
    elif request.method == 'POST':
        usuario = request.POST.get('usuario')
        senha = request.POST.get('senha')

        user = authenticate(username=usuario, password=senha)

        if user:
            login(request, user)
            return redirect(reverse('home'))
        else:
            return redirect(reverse('login'))


def cadastro(request):
    if request.method == 'GET':
        return render(request, 'cadastro.html')
    
    elif request.method == 'POST':
        usuario = request.POST.get('usuario')
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        user = User.objects.filter(username=usuario).first()

        if user:
            return redirect(reverse('cadastro'))
        
        user = User.objects.create_user(username=usuario, email=email, password=senha)
        user.save()

        return redirect(reverse('login'))
        
def logout_user(request):
    logout(request)
    return redirect(reverse('login'))
        

        



