# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Description',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first', models.CharField(max_length=30)),
                ('last', models.CharField(max_length=30)),
            ],
        ),
        migrations.AlterField(
            model_name='building',
            name='description',
            field=models.ForeignKey(to='app.Description'),
        ),
    ]
