# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20150621_0655'),
    ]

    operations = [
        migrations.AlterField(
            model_name='building',
            name='description',
            field=models.TextField(max_length=1000),
        ),
        migrations.DeleteModel(
            name='Description',
        ),
    ]
