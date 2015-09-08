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
                ('clave', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('valor', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='slink',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('clave', models.CharField(max_length=16, unique=True)),
                ('url', models.URLField()),
                ('fecha', models.DateTimeField(auto_now=True)),
                ('clicks', models.PositiveIntegerField(default=0)),
            ],
        ),
    ]
