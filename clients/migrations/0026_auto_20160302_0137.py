# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0018_training'),
        ('clients', '0025_clubcardtrains'),
    ]

    operations = [
        migrations.AddField(
            model_name='clientclubcard',
            name='bonus_amount',
            field=models.FloatField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='clientclubcard',
            name='bonus_type',
            field=models.ForeignKey(related_name=b'club_card_bonus_type', blank=True, to='products.Discount', null=True),
            preserve_default=True,
        ),
    ]
