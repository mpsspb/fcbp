# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0017_auto_20170115_0135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='extra_uid',
            field=models.CharField(max_length=36, null=True, blank=True),
        ),
    ]
