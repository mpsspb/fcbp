# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0028_training_order_num'),
    ]

    operations = [
        migrations.AddField(
            model_name='personal',
            name='club_card_only',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
