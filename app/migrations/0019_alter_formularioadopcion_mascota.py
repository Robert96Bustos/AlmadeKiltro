# Generated by Django 4.0.4 on 2022-06-11 22:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0018_formularioadopcion_mascota'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formularioadopcion',
            name='mascota',
            field=models.ForeignKey(default=13, on_delete=django.db.models.deletion.PROTECT, to='app.mascota'),
        ),
    ]