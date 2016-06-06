# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-06 15:03
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20160606_1018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slink',
            name='slug',
            field=models.CharField(blank=True, max_length=16, unique=True, validators=[django.core.validators.MaxLengthValidator(16)]),
        ),
    ]
