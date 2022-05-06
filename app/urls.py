from django.urls import path
from .views import home, login, mascotas

urlpatterns = [
    path('', home, name="home"),
    path('login/', login, name="login"),
    path('mascotas/', mascotas, name="mascotas"),
]