from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, Request

class RegistroForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Requerido. Ingresa una dirección de correo electrónico válida.')

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2')

class LoginForm(forms.Form):
    email = forms.EmailField(label="Correo Electrónico", max_length=254, required=True)
    password = forms.CharField(label="Contraseña", widget=forms.PasswordInput)

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'first_name', 'last_name')

class RequestForm(forms.ModelForm):
    class Meta:
        model = Request
        fields = ('description', 'file')
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
        }