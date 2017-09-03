# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0030_auto_20170730_1732'),
    ]

    operations = [
        migrations.AddField(
            model_name='personal',
            name='period_activation',
            field=models.IntegerField(default=0, blank=True),
            preserve_default=True,
        ),
    ]
