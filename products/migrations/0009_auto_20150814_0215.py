# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_sport_ticket'),
    ]

    operations = [
        migrations.AddField(
            model_name='sport',
            name='is_active',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='ticket',
            name='is_active',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
    ]
