# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0017_auto_20160128_0210'),
        ('clients', '0021_auto_20160126_0051'),
    ]

    operations = [
        migrations.AddField(
            model_name='clientclubcard',
            name='discount',
            field=models.ForeignKey(blank=True, to='products.Discount', null=True),
            preserve_default=True,
        ),
    ]
