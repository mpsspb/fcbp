# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0018_training'),
        ('clients', '0033_auto_20160525_2238'),
    ]

    operations = [
        migrations.AddField(
            model_name='clientaquaaerobics',
            name='bonus_amount',
            field=models.FloatField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='clientaquaaerobics',
            name='bonus_type',
            field=models.ForeignKey(related_name=b'aqua_bonus_type', blank=True, to='products.Discount', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='clientaquaaerobics',
            name='discount_amount',
            field=models.FloatField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='clientaquaaerobics',
            name='discount_type',
            field=models.ForeignKey(blank=True, to='products.Discount', null=True),
            preserve_default=True,
        ),
    ]
