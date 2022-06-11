from cgitb import reset
from pickle import NONE
from django.http import QueryDict
from django.shortcuts import render, redirect, get_object_or_404
from .models import Mascota, MascotaDesaparecida
from .forms import ContactoForm, MascotaForm, CustomUserCreationForm, MascotaDesaparecidaForm, FormularioAdopcionForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.db.models import Q
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
def home(request):
    queryset = request.POST.get("buscar")
    queryset2 = request.POST.get("buscar2")
    
    filtro = []
    if queryset != None and queryset != '-1':
        filtro.append(('especie' , int(queryset)))
    if queryset2 != None and queryset2 != '-1':
        filtro.append(('sexo' , int(queryset2)))

    mascotas = Mascota.objects.all()


    if len(filtro) > 0 :
        mascotas = Mascota.objects.filter(
            *filtro
    )
    data = {
        'mascotas': mascotas,
        'mensaje': "Lo sentimos no hay mascotas"
    }

    return render(request, 'app/home.html', data)

def mascotasDesaparecidas(request):
    queryset = request.POST.get("buscar")
    
    filtro=[]
    if queryset != None and queryset != '-1':
        filtro.append(('tipo_publicacion', int(queryset)))

    mascotas = MascotaDesaparecida.objects.all()

    if len(filtro)>0:
        mascotas = MascotaDesaparecida.objects.filter(
            *filtro
        )

    data = {
        'mascotas': mascotas
    }
    return render(request, 'app/mascotas_desaparecidas/mascotas.html', data)

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
            messages.success(request, "Mascota registrada")
        else:
            data["form"] = formulario
    return render(request, 'app/mascota/agregar.html', data)

def formulario_adopcion(request):
    data = {
        'form': FormularioAdopcionForm()
    }
    if request.method =='POST':
        form = FormularioAdopcionForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()

            subject = "Solicitud de Adopción - Mascota Numero:" + " " + request.POST["mascota"]
            message = request.POST["nombres"]+" "+ request.POST["apellidos"]+ " "+ request.POST["telefono"]
            email_from = settings.EMAIL_HOST_USER
            recipient_list=["dekiltroalma@gmail.com"]

            send_mail(subject, message, email_from, recipient_list)

            messages.success(request, "Solicitud de adopción enviada correctamente, uno de nuestros voluntarios se comunicara con usted.")
            return render(request,"app/nosotros.html")
        else:
            data["form"]=form
    return render(request, 'app/mascota/form_adopcion.html', data)


def agregar_mascota_desaparecida(request):
    data = {
        'form': MascotaDesaparecidaForm()
    }
    if request.method =='POST':
        form = MascotaDesaparecidaForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Aviso de mascota encontrada con exito.")
        else:
            data["form"]=form
    return render(request, 'app/mascotas_desaparecidas/agregar.html', data)


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
            messages.success(request, "Modificado correctamente")
            return redirect(to="listar_mascotas")
            data["form"] = formulario
    return render(request, 'app/mascota/modificar.html', data)

def eliminar_mascota(request, id):
    mascota = get_object_or_404(Mascota, id=id)
    mascota.delete()
    messages.success(request, "Eliminado correctamente")
    return redirect(to="listar_mascotas")

# Registro de usuario
def registro(request):
    data = {
        'form': CustomUserCreationForm()
    }
    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request, user)
            messages.success(request, "Registro exitoso")
            return redirect(to="home")
        data["form"] = formulario
    return render(request, 'registration/registro.html', data)

def nosotros(request):
    return render(request, 'app/nosotros.html')