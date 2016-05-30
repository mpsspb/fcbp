# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0035_freezeaqua'),
    ]

    operations = [
        migrations.AddField(
            model_name='clientaquaaerobics',
            name='is_paid_activate',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='clientaquaaerobics',
            name='paid_activate_amount',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
