# Generated by Django 4.0.4 on 2022-06-11 22:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0016_remove_formularioadopcion_estado_solicitud'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='formularioadopcion',
            name='mascota',
        ),
    ]
