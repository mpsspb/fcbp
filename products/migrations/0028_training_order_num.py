# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0027_discount_is_best_loyalty'),
    ]

    operations = [
        migrations.AddField(
            model_name='training',
            name='order_num',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
