from django import forms
from .models import Contacto, Mascota

class ContactoForm(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = '__all__'

class MascotaForm(forms.ModelForm):
    class Meta:
        model = Mascota
        fields = '__all__'