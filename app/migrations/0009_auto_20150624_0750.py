# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_auto_20150624_0747'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='building',
            name='sborka',
        ),
        migrations.AddField(
            model_name='photo',
            name='sborka',
            field=models.ManyToManyField(to='app.Building'),
        ),
    ]
