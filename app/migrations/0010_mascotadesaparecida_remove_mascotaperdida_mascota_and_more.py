# Generated by Django 4.0.4 on 2022-06-10 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_delete_mascotaadopcion'),
    ]

    operations = [
        migrations.CreateModel(
            name='MascotaDesaparecida',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_desaparecida', models.CharField(max_length=250)),
                ('imagen', models.ImageField(null=True, upload_to='mascotas_desaparecidas')),
                ('fecha_desaparecida', models.DateField()),
                ('fecha_publicacion', models.DateField(auto_now=True)),
                ('region', models.CharField(max_length=250)),
                ('comuna', models.CharField(max_length=250)),
                ('lugar', models.CharField(max_length=250)),
                ('descripcion', models.TextField()),
                ('tipo_publicacion', models.IntegerField(choices=[[0, 'Mascota Perdida'], [1, 'Mascota Encontrada']])),
            ],
        ),
        migrations.RemoveField(
            model_name='mascotaperdida',
            name='mascota',
        ),
        migrations.DeleteModel(
            name='MascotaEncontrada',
        ),
        migrations.DeleteModel(
            name='MascotaPerdida',
        ),
    ]