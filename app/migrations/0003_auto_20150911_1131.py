# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime

def data_migrations(apps, schema_editor):
    slink = apps.get_model("app", "slink")
    for s in slink.objects.all():
        s.slug = s.clave
        s.creado = s.fecha
        s.modificado = s.fecha
        s.save()

class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20150911_1111'),
    ]

    operations = [
        migrations.AddField(
            model_name='slink',
            name='creado',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 11, 11, 31, 32, 869695)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='slink',
            name='modificado',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 11, 11, 31, 37, 573579)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='slink',
            name='slug',
            field=models.SlugField(max_length=16, default=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='slink',
            name='id',
            field=models.PositiveIntegerField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True),
        ),
        migrations.RunPython(data_migrations),
        migrations.RemoveField(
            model_name='slink',
            name='clave',
        ),
        migrations.RemoveField(
            model_name='slink',
            name='fecha',
        ),
    ]
