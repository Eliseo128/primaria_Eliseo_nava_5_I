# Generated by Django 5.1 on 2024-10-05 14:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AlumnoT',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Apaterno', models.CharField(max_length=50, verbose_name='Apellido paterno')),
                ('Amaterno', models.CharField(max_length=50, verbose_name='Apellido materno')),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre')),
                ('fecha_nacimiento', models.DateField(verbose_name='Fecha Nacimiento')),
                ('fecha_ingreso', models.DateField(verbose_name='Fecha Ingreso')),
            ],
            options={
                'verbose_name': 'Alumno',
                'verbose_name_plural': 'Alumnos',
                'db_table': 'Alumnos',
            },
        ),
        migrations.CreateModel(
            name='Frase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comentario', models.TextField(max_length=400, verbose_name='Comentario')),
                ('Alumno_fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.alumnot')),
            ],
        ),
    ]
