# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20150911_1131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slink',
            name='creado',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='slink',
            name='modificado',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='slink',
            name='slug',
            field=models.SlugField(unique=True, max_length=16),
        ),
    ]
