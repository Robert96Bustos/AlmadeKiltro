from django.db import models

# Create your models here.

opciones_nombre_raza = [
    [0, "Kiltro"],
    [1, "Mestizo"],
    [2, "Poodle"],
    [3, "Galgo"],
    [4, "Otro"]
]

class Raza(models.Model):
    nombre_raza = models.IntegerField(choices=opciones_nombre_raza)

    def __str__(self):
        return self.nombre_raza

# Opciones especie
opciones_especie = [
    [0, "Perro"],
    [1, "Gato"]
]

class Especie(models.Model):
    nombre_especie = models.IntegerField(choices=opciones_especie)

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
    nombre_mascota_perdida = models.CharField(max_length=250)
    contacto_perdida = models.CharField(max_length=250)
    fecha_extravio = models.DateField()
    fecha_publicacion = models.DateField()
    mascota = models.ForeignKey(Mascota, on_delete=models.PROTECT)

    def __str__(self):
        return self.nombre_mascota_perdida

class MascotaEncontrada(models.Model):
    nombre_mascota_encontrada = models.CharField(max_length=250)
    fecha_encontrada = models.DateField()
    fecha_publicacion = models.DateField()
    contacto_encontrada = models.CharField(max_length=250)
    mascota = models.ForeignKey(Mascota, on_delete=models.PROTECT)

    def __str__(self):
        return self.nombre_mascota_encontrada

class MascotaAdopcion(models.Model):
    nombre_mascota_adopcion = models.CharField(max_length=250)
    peso = models.IntegerField()
    mascota = models.ForeignKey(Mascota, on_delete=models.PROTECT)

    def __str__(self):
        return self.nombre_mascota_adopcion

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
    fecha_solicitud = models.DateField()
    estado_solicitud = models.IntegerField()
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