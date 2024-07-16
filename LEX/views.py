from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from .forms import RegistroForm, LoginForm, UserUpdateForm, RequestForm
from .models import CustomUser, Request

def register(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')
            user = authenticate(email=email, password=password)
            auth_login(request, user)
            return redirect('profile')
    else:
        form = RegistroForm()
    return render(request, 'LEX/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(email=email, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('profile')
            else:
                form.add_error(None, 'El correo electrónico y/o contraseña son incorrectos.')
    else:
        form = LoginForm()
    return render(request, 'LEX/login.html', {'form': form})

@login_required
def user_logout(request):
    auth_logout(request)
    return redirect('login')

@login_required
def profile(request):
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UserUpdateForm(instance=request.user)
    return render(request, 'LEX/profile.html', {'form': form})

@login_required
def create_request(request):
    if request.method == 'POST':
        form = RequestForm(request.POST, request.FILES)
        if form.is_valid():
            request_instance = form.save(commit=False)
            request_instance.user = request.user
            request_instance.save()
            return redirect('profile')
    else:
        form = RequestForm()
    return render(request, 'LEX/create_request.html', {'form': form})

@login_required
def admin_requests_view(request):
    if not request.user.is_staff:
        return redirect('profile')
    requests = Request.objects.all()
    return render(request, 'LEX/admin_requests.html', {'requests': requests})

def index(request):
    context = {}
    return render(request, 'LEX/index.html', context)
