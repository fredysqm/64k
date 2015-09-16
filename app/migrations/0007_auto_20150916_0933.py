# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20150916_0932'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slink',
            name='id',
            field=models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True),
        ),
    ]
