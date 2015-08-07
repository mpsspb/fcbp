# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_period_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='clubcard',
            name='freeze_times',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
