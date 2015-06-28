# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20150623_1820'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo2',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('photo2', models.ImageField(upload_to=b'.')),
                ('proekt', models.ForeignKey(to='app.Building')),
            ],
        ),
        migrations.CreateModel(
            name='Photo3',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('photo3', models.ImageField(upload_to=b'.')),
                ('proekt', models.ForeignKey(to='app.Building')),
            ],
        ),
        migrations.CreateModel(
            name='Photo4',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('photo4', models.ImageField(upload_to=b'.')),
                ('proekt', models.ForeignKey(to='app.Building')),
            ],
        ),
        migrations.CreateModel(
            name='Photo5',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('photo5', models.ImageField(upload_to=b'.')),
                ('proekt', models.ForeignKey(to='app.Building')),
            ],
        ),
        migrations.RenameModel(
            old_name='Photo',
            new_name='Photo1',
        ),
        migrations.RenameField(
            model_name='photo1',
            old_name='photo',
            new_name='photo1',
        ),
    ]
