# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0014_auto_20161023_2108'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='extra_text',
            field=models.CharField(max_length=150, null=True, blank=True),
            preserve_default=True,
        ),
    ]
