# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations

def data_migrations(apps, schema_editor):
    slink = apps.get_model("app", "slink")
    i = 1
    for s in slink.objects.all():
        s.id = i
        s.save()
        i += 1

class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='slink',
            name='id',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='slink',
            name='clave',
            field=models.SlugField(max_length=16, serialize=False, primary_key=True),
        ),
        migrations.RunPython(data_migrations),
    ]
