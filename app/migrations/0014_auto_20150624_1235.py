# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_photo_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photo',
            name='sborka',
        ),
        migrations.AddField(
            model_name='photo',
            name='sborka',
            field=models.ForeignKey(to='app.Building', null=True),
        ),
    ]
