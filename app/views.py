from django.shortcuts import render, redirect, get_object_or_404
from .models import Mascota
from .forms import ContactoForm, MascotaForm

# Create your views here.

def home(request):
    return render(request, 'app/home.html')

def login(request):
    return render(request, 'app/login.html')

def mascotas(request):
    mascotas = Mascota.objects.all()
    data = {
        'mascotas': mascotas
    }
    return render(request, 'app/mascotas.html', data)

def contacto(request):
    data = {
        'form': ContactoForm()
    }
    if request.method == 'POST':
        formulario = ContactoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Mensaje enviado"
        else:
            data["form"] = formulario

    return render(request, 'app/contacto.html', data)

# CRUD MASCOTA
def agregar_mascota(request):
    data = {
        'form': MascotaForm()
    }
    if request.method == 'POST':
        formulario =MascotaForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Guardado correctamente"
        else:
            data["form"] = formulario
    return render(request, 'app/mascota/agregar.html', data)

def listar_mascotas(request):
    mascotas = Mascota.objects.all()
    data = {
        'mascotas': mascotas
    }
    return render(request, 'app/mascota/listar.html', data)

def modificar_mascota(request, id):
    mascota = get_object_or_404(Mascota, id=id)
    data = {
        'form': MascotaForm(instance=mascota)
    }
    if request.method == 'POST':
        formulario = MascotaForm(data=request.POST, instance=mascota, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="listar_mascotas")
            data["form"] = formulario
    return render(request, 'app/mascota/modificar.html', data)

def eliminar_mascota(request, id):
    mascota = get_object_or_404(Mascota, id=id)
    mascota.delete()
    return redirect(to="listar_mascotas")
