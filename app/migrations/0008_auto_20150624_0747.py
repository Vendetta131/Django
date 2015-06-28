# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20150623_1847'),
    ]

    operations = [
        migrations.RenameField(
            model_name='photo',
            old_name='photo1',
            new_name='one',
        ),
        migrations.RenameField(
            model_name='photo',
            old_name='photo2',
            new_name='second',
        ),
        migrations.RenameField(
            model_name='photo',
            old_name='photo3',
            new_name='third',
        ),
        migrations.RemoveField(
            model_name='photo',
            name='photo4',
        ),
        migrations.RemoveField(
            model_name='photo',
            name='photo5',
        ),
        migrations.RemoveField(
            model_name='photo',
            name='proekt',
        ),
        migrations.AddField(
            model_name='building',
            name='sborka',
            field=models.ManyToManyField(to='app.Photo'),
        ),
    ]
