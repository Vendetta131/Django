# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_auto_20150625_1104'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photo',
            name='sevent',
        ),
    ]
