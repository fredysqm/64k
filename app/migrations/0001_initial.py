# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-07 16:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='opcion',
            fields=[
                ('clave', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('valor', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name_plural': 'opciones',
            },
        ),
        migrations.CreateModel(
            name='slink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.CharField(max_length=16, unique=True)),
                ('url', models.URLField(verbose_name='URL Largo')),
                ('visitas', models.PositiveIntegerField(default=0)),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('acceso', models.DateTimeField(auto_now=True)),
                ('estado', models.CharField(choices=[('A', 'Activo'), ('I', 'Inactivo'), ('D', 'Deshabilitado')], default='A', max_length=1)),
            ],
        ),
    ]
