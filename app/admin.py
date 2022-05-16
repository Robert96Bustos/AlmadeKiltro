from django.contrib import admin
from .models import Raza, Especie, Mascota, MascotaPerdida, MascotaEncontrada, MascotaAdopcion, FormularioAdopcion, Fundacion, Contacto
# Register your models here.

#
class MascotaAdmin(admin.ModelAdmin):
    list_display = ["nombre_mascota", "edad_mascota", "sexo", "tamaño", "peso", "especie", "raza", "descripcion", "imagen"]
    list_editable = ["tamaño", "raza"]
    search_fields = ["nombre_mascota"]
    list_filter = ["sexo", "especie", "raza"]
    list_per_page = 10

admin.site.register(Raza)
admin.site.register(Especie)
admin.site.register(Mascota,MascotaAdmin)
admin.site.register(MascotaPerdida)
admin.site.register(MascotaEncontrada)
admin.site.register(MascotaAdopcion)
admin.site.register(FormularioAdopcion)
admin.site.register(Fundacion)
admin.site.register(Contacto)