from dataclasses import field
from operator import attrgetter
from tkinter import Widget
from turtle import width
from django import forms
from .models import Contacto, Mascota, MascotaDesaparecida, FormularioAdopcion
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class ContactoForm(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = '__all__'

class MascotaForm(forms.ModelForm):
    class Meta:
        model = Mascota
        fields = '__all__'

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email", "password1", "password2"]

class MascotaDesaparecidaForm(forms.ModelForm):
    class Meta:
        model = MascotaDesaparecida
        fields = '__all__'

class FormularioAdopcionForm(forms.ModelForm):
    class Meta:
        model = FormularioAdopcion
        fields = '__all__'