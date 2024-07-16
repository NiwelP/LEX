# LEX/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser

class RegistroForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Requerido. Ingresa una dirección de correo electrónico válida.')

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2')

class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Correo electrónico', max_length=254)
    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
