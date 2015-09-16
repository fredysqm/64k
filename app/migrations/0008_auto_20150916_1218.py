# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20150916_0933'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slink',
            name='slug',
            field=models.CharField(max_length=16, unique=True),
        ),
    ]
