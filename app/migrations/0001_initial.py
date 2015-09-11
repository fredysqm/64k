# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='opciones',
            fields=[
                ('clave', models.CharField(primary_key=True, max_length=20, serialize=False)),
                ('valor', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='slink',
            fields=[
                ('clave', models.CharField(primary_key=True, max_length=16, serialize=False)),
                ('url', models.URLField(unique=True)),
                ('fecha', models.DateTimeField(auto_now=True)),
                ('clicks', models.PositiveIntegerField(default=0)),
            ],
        ),
    ]
