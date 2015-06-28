# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20150621_0952'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('photo', models.ImageField(upload_to=b'.')),
            ],
        ),
        migrations.RenameField(
            model_name='building',
            old_name='photo',
            new_name='glav',
        ),
        migrations.AddField(
            model_name='photo',
            name='proekt',
            field=models.ForeignKey(to='app.Building'),
        ),
    ]
