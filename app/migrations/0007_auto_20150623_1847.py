# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20150623_1843'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photo',
            name='proekt',
        ),
        migrations.AddField(
            model_name='photo',
            name='proekt',
            field=models.ManyToManyField(to='app.Building'),
        ),
    ]
