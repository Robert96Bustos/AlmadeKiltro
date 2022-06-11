from tkinter import Widget
from django.db import models
import datetime

class Raza(models.Model):
    nombre_raza = models.CharField(max_length=250)

    def __str__(self):
        return self.nombre_raza


class Especie(models.Model):
    nombre_especie = models.CharField(max_length=250)

    def __str__(self):
        return self.nombre_especie

# Opciones sexo de la mascota
opciones_sexo = [
    [0, "Hembra"],
    [1, "Macho"]
]

# Opciones tamaño de la mascota
opciones_tamaño = [
    [0, "Pequeño"],
    [1, "Mediano"],
    [2, "Grande"]
]

class Mascota(models.Model):
    nombre_mascota = models.CharField(max_length=250)
    imagen = models.ImageField(upload_to="mascota", null=True)
    edad_mascota = models.CharField(max_length=250)
    sexo = models.IntegerField(choices=opciones_sexo)
    descripcion = models.TextField()
    tamaño = models.IntegerField(choices=opciones_tamaño)
    peso = models.CharField(max_length=250)
    especie = models.ForeignKey(Especie, on_delete=models.PROTECT)
    raza = models.ForeignKey(Raza, on_delete=models.PROTECT)
   

    def __str__(self):
        return self.nombre_mascota

# Opciones tipo publicacion
opciones_publicacion = [
    [0, "Mascota Perdida"],
    [1, "Mascota Encontrada"]
]
class MascotaDesaparecida(models.Model):
    nombre_desaparecida = models.CharField(max_length=250)
    imagen = models.ImageField(upload_to="mascotas_desaparecidas", null = True)
    fecha_desaparecida = models.DateField()
    fecha_publicacion = models.DateField(auto_now=True)
    region = models.CharField(max_length=250)
    comuna = models.CharField(max_length=250)
    lugar = models.CharField(max_length=250)
    numero_contacto = models.IntegerField(blank=True, null=True)
    descripcion = models.TextField()
    tipo_publicacion = models.IntegerField(choices=opciones_publicacion)

    def __str__(self):
        return self.nombre_desaparecida

# Opciones tipo vivienda
opciones_tipo_vivienda = [
    [0, "Casa"],
    [1, "Departamento"]
]
# Opciones tipo vivienda
opciones_cantidad_mascotas = [
    [0, "0"],
    [1, "1"],
    [2, "2"],
    [3, "Más de 2"]
]

class FormularioAdopcion(models.Model):
    nombres = models.CharField(max_length=250)
    apellidos = models.CharField(max_length=250)
    edad = models.IntegerField()
    telefono = models.IntegerField()
    tipo_vivienda = models.IntegerField(choices=opciones_tipo_vivienda)
    direccion = models.CharField(max_length=250)
    otra_mascota = models.BooleanField()
    fecha_solicitud = models.DateField(auto_now=True)
    cantidad_mascotas = models.IntegerField(choices=opciones_cantidad_mascotas)
    mascota = models.ForeignKey(Mascota, on_delete=models.PROTECT)

    def __str__(self):
        return self.nombres

class Fundacion(models.Model):
    nombre_fundacion = models.CharField(max_length=250)
    direccion_fundacion = models.CharField(max_length=250)
    contacto_fundacion = models.CharField(max_length=250)

    def __str__(self):
        return self.nombre_fundacion

# CONTACTO
opciones_consulta = [
    [0, "Consulta"],
    [1, "Reclamo"],
    [2, "Sugerencia"],
    [3, "Agradecimientos"]
]

class Contacto(models.Model):
    nombre =  models.CharField(max_length=250)
    correo = models.EmailField()
    tipo_consulta = models.IntegerField(choices=opciones_consulta)
    mensaje = models.TextField()
    avisos = models.BooleanField()

    def __str__(self):
        return self.nombre