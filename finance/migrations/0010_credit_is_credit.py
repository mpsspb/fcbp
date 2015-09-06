# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0009_auto_20150830_1833'),
    ]

    operations = [
        migrations.AddField(
            model_name='credit',
            name='is_credit',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
