# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20150623_1826'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('photo1', models.ImageField(upload_to=b'.')),
                ('photo2', models.ImageField(upload_to=b'.')),
                ('photo3', models.ImageField(upload_to=b'.')),
                ('photo4', models.ImageField(upload_to=b'.')),
                ('photo5', models.ImageField(upload_to=b'.')),
                ('proekt', models.ForeignKey(to='app.Building')),
            ],
        ),
        migrations.RemoveField(
            model_name='photo1',
            name='proekt',
        ),
        migrations.RemoveField(
            model_name='photo2',
            name='proekt',
        ),
        migrations.RemoveField(
            model_name='photo3',
            name='proekt',
        ),
        migrations.RemoveField(
            model_name='photo4',
            name='proekt',
        ),
        migrations.RemoveField(
            model_name='photo5',
            name='proekt',
        ),
        migrations.DeleteModel(
            name='Photo1',
        ),
        migrations.DeleteModel(
            name='Photo2',
        ),
        migrations.DeleteModel(
            name='Photo3',
        ),
        migrations.DeleteModel(
            name='Photo4',
        ),
        migrations.DeleteModel(
            name='Photo5',
        ),
    ]
