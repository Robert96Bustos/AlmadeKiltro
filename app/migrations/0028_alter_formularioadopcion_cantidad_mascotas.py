# Generated by Django 4.0.4 on 2022-06-16 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0027_alter_formularioadopcion_tipo_vivienda'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formularioadopcion',
            name='cantidad_mascotas',
            field=models.CharField(choices=[['0', '0'], ['1', '1'], ['2', '2'], ['3', 'Más de 2']], max_length=20),
        ),
    ]
