from re import template
from django.urls import path
from .views import home, contacto, agregar_mascota, listar_mascotas, modificar_mascota, eliminar_mascota, nosotros, registro
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', home, name="home"),
    path('contacto/', contacto, name="contacto"),
    path('agregar-mascota/', agregar_mascota, name="agregar_mascota"),
    path('listar-mascotas/', listar_mascotas, name="listar_mascotas"),
    path('modificar-mascota/<id>/', modificar_mascota, name="modificar_mascota"),
    path('eliminar-mascota/<id>/', eliminar_mascota, name="eliminar_mascota"),
    path('registro/', registro, name="registro"),
    path('quienes-somos/', nosotros, name="nosotros"),
    path('accounts/login/', auth_views.LoginView.as_view(template_name="registration/login.html")),

    path('reset_password/', auth_views.PasswordResetView.as_view(
        template_name="registration/recuperar_contraseña.html"
    ), name="reset_password"),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(
        template_name="registration/mensaje_cambio_pw.html"
    ), name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name="registration/cambio_pw_form.html"
    ), name="password_reset_confirm"),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(
        template_name="registration/cambio_pw_done.html"
    ), name="password_reset_complete"),

]