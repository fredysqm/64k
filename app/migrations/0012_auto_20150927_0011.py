# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_auto_20150918_0844'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slink',
            name='url',
            field=models.URLField(verbose_name='URL Largo'),
        ),
    ]
