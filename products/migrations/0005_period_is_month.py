# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20150812_1736'),
    ]

    operations = [
        migrations.AddField(
            model_name='period',
            name='is_month',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
    ]
