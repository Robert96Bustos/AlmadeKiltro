from django.urls import path
from .views import home, login, mascotas, contacto, agregar_mascota, listar_mascotas, modificar_mascota, eliminar_mascota

urlpatterns = [
    path('', home, name="home"),
    path('login/', login, name="login"),
    path('mascotas/', mascotas, name="mascotas"),
    path('contacto/', contacto, name="contacto"),
    path('agregar-mascota/', agregar_mascota, name="agregar_mascota"),
    path('listar-mascotas/', listar_mascotas, name="listar_mascotas"),
    path('modificar-mascota/<id>/', modificar_mascota, name="modificar_mascota"),
    path('eliminar_mascota/<id>/', eliminar_mascota, name="eliminar_mascota"),
]