# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_auto_20150917_1514'),
    ]

    operations = [
        migrations.RenameField(
            model_name='slink',
            old_name='clicks',
            new_name='visitas',
        ),
    ]
