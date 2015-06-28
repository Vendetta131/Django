# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_auto_20150624_0809'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='fifth',
            field=models.ImageField(upload_to=b'.', blank=True),
        ),
        migrations.AddField(
            model_name='photo',
            name='fourth',
            field=models.ImageField(upload_to=b'.', blank=True),
        ),
        migrations.AddField(
            model_name='photo',
            name='sevent',
            field=models.ImageField(upload_to=b'.', blank=True),
        ),
        migrations.AddField(
            model_name='photo',
            name='sixth',
            field=models.ImageField(upload_to=b'.', blank=True),
        ),
        migrations.AlterField(
            model_name='photo',
            name='one',
            field=models.ImageField(upload_to=b'.', blank=True),
        ),
    ]
