# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='opcion',
            fields=[
                ('clave', models.CharField(primary_key=True, serialize=False, max_length=20)),
                ('valor', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name_plural': 'opciones',
            },
        ),
        migrations.CreateModel(
            name='slink',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('slug', models.CharField(max_length=16, unique=True)),
                ('url', models.URLField(verbose_name='URL Largo')),
                ('visitas', models.PositiveIntegerField(default=0)),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('acceso', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
