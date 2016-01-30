# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0023_auto_20160129_0128'),
    ]

    operations = [
        migrations.AddField(
            model_name='clientclubcard',
            name='discount_amount',
            field=models.FloatField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
