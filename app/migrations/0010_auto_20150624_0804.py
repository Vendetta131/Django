# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_auto_20150624_0750'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='one',
            field=models.ImageField(upload_to=b'.', blank=True),
        ),
    ]
