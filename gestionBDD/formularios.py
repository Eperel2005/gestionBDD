from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class UserRegisterForm(UserCreationForm):
    username=forms.CharField(label="Nombre del usuario")
    email=forms.CharField(label="Correo", widget=forms.EmailInput)
    password1=forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2=forms.CharField(label="Confirme contraseña", widget=forms.PasswordInput)

    class Meta:
        model = User

        fields= ["username", "email", "password1", "password2"]
        help_texts = {k:"" for k in fields}