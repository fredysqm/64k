# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_auto_20150916_1303'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='opcion',
            options={'verbose_name_plural': 'opciones'},
        ),
        migrations.AlterField(
            model_name='slink',
            name='url',
            field=models.URLField(unique=True, verbose_name='URL Largo'),
        ),
    ]
