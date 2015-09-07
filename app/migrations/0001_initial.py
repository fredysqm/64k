# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='options',
            fields=[
                ('name', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('value', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='slink',
            fields=[
                ('keyword', models.CharField(max_length=16, primary_key=True, serialize=False)),
                ('url', models.URLField()),
                ('fecha', models.DateTimeField(auto_now=True)),
                ('clicks', models.PositiveIntegerField(default=0)),
            ],
        ),
    ]
