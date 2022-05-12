from django.db import models

# Create your models here.

# Opciones raza !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
class Raza(models.Model):
    nombre_raza = models.CharField(max_length=250)

    def __str__(self):
        return self.nombre_raza

# Opciones especie
opciones_especie = [
    [0, "Perro"],
    [1, "Gato"]
]

class Especie(models.Model):
    nombre_especie = models.IntegerField(choices=opciones_especies)

    def __str__(self):
        return self.nombre_especie

# Opciones sexo de la mascota
opciones_sexo = [
    [0, "M"],
    [1, "F"]
]

# Opciones tamaño de la mascota
opciones_tamaño = [
    [0, "Pequeño"],
    [1, "Mediano"],
    [2, "Grande"]
]

class Mascota(models.Model):
    nombre_mascota = models.CharField(max_length=250)
    edad_mascota = models.IntegerField()
    sexo = models.IntegerField(choices=opciones_sexo)
    descripcion = models.TextField()
    tamaño = models.IntegerField(choices=opciones_tamaño)
    peso = models.IntegerField()
    raza = models.ForeignKey(Raza, on_delete=models.PROTECT)
    especie = models.ForeignKey(Especie, on_delete=models.PROTECT)

    def __str__(self):
        return self.nombre_mascota

class MascotaPerdida(models.Model):
    contacto_perdida = models.CharField(max_length=250)
    fecha_extravio = models.DateField()
    fecha_publicacion = models.DateField()
    mascota = models.ForeignKey(Mascota, on_delete=models.PROTECT)

    def __str__(self):
        return self.

class MascotaEncontrada(models.Model):
    fecha_encontrada = models.DateField()
    fecha_publicacion = models.DateField()
    contacto_encontrada = models.CharField(max_length=250)
    mascota = models.ForeignKey(Mascota, on_delete=models.PROTECT)

    def __str__(self):
        return self.

class MascotaAdopcion(models.Model):
    peso = models.IntegerField()
    mascota = models.ForeignKey(Mascota, on_delete=models.PROTECT)

    def __str__(self):
        return self.

class FormularioAdopcion(models.Model):
    nombres = models.CharField(max_length=250)
    apellidos = models.CharField(max_length=250)
    edad = models.IntegerField()
    telefono = models.IntegerField()
    tipo_vivienda = = models.IntegerField()
    direccion = models.CharField(max_length=250)
    otra_mascota = models.BooleanField()
    fecha_solicitud = models.DateField()
    estado_solicitud = = models.IntegerField()
    cantidad_mascotas = models.IntegerField()
    mascota = models.ForeignKey(Mascota, on_delete=models.PROTECT)

    def __str__(self):
        return self.nombres

class Fundacion(models.Model):
    nombre_fundacion = models.CharField(max_length=250)
    direccion_fundacion = models.CharField(max_length=250)
    contacto_fundacion = models.CharField(max_length=250)

    def __str__(self):
        return self.nombre_fundacion