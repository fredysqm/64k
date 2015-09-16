# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_auto_20150916_1218'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='opciones',
            new_name='opcion',
        ),
    ]
