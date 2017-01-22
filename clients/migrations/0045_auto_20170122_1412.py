# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0044_auto_20161114_2309'),
    ]

    operations = [
        migrations.AddField(
            model_name='freezeclubcard',
            name='is_extra',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='prolongationclubcard',
            name='is_extra',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
