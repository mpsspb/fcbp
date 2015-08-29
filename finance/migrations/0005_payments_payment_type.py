# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0004_auto_20150829_1628'),
    ]

    operations = [
        migrations.AddField(
            model_name='payments',
            name='payment_type',
            field=models.SmallIntegerField(default=1),
            preserve_default=True,
        ),
    ]
