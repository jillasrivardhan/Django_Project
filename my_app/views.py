from django.shortcuts import redirect, render
from . import models

# Create your views here.

def index(request):
    return render(request, 'index.html')

def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            user = models.UserRegistration.objects.get(email=email, password=password)
            request.session['user'] = user.email
            return  redirect('dashboard')
        except:
            return render(request, 'login.html', {'msg': 'Invalid email or password'})
           


def register(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        models.UserRegistration.objects.create(name=name, email=email, password=password)
        return render(request, 'Register.html', {'msg': 'Registration successful. Please login.'})
    return render(request, 'Register.html')


def dashboard(request):
    if 'user'  not in request.session:
       return redirect('login')
    return render(request, 'dashboard.html')

def logout(request):
    request.session.flush()
    return redirect('login')