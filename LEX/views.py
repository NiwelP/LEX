# LEX/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.decorators import login_required
from .forms import RegistroForm, LoginForm

def register(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')
            user = authenticate(email=email, password=password)
            auth_login(request, user)
            return redirect('clienteView')
    else:
        form = RegistroForm()
    return render(request, 'LEX/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(email=email, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('clienteView')
            else:
                form.add_error(None, 'El correo electrónico y/o contraseña son incorrectos.')
    else:
        form = LoginForm()
    return render(request, 'LEX/login.html', {'form': form})

@login_required
def clienteView(request):
    return render(request, 'LEX/clienteView.html')

def index(request):
    context = {}
    return render(request, 'LEX/index.html', context)
