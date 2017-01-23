# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0045_auto_20170122_1412'),
    ]

    operations = [
        migrations.AddField(
            model_name='freezeclubcard',
            name='note',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='prolongationclubcard',
            name='note',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
