# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_clubcard_freeze_times'),
    ]

    operations = [
        migrations.AlterField(
            model_name='period',
            name='value',
            field=models.SmallIntegerField(unique=True),
        ),
    ]
