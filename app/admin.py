from django.contrib import admin
from .models import Raza, Especie, Mascota, MascotaPerdida, MascotaEncontrada, MascotaAdopcion, FormularioAdopcion, Fundacion
# Register your models here.



admin.site.register(Raza)
admin.site.register(Especie)
admin.site.register(Mascota)
admin.site.register(MascotaPerdida)
admin.site.register(MascotaEncontrada)
admin.site.register(MascotaAdopcion)
admin.site.register(FormularioAdopcion)
admin.site.register(Fundacion)