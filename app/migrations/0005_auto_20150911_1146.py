# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20150911_1135'),
    ]

    operations = [
        migrations.RenameField(
            model_name='slink',
            old_name='modificado',
            new_name='acceso',
        ),
    ]
