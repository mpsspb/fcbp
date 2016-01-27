# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0015_auto_20151124_0055'),
    ]

    operations = [
        migrations.AddField(
            model_name='discount',
            name='description',
            field=models.CharField(default='we', max_length=150),
            preserve_default=False,
        ),
    ]
