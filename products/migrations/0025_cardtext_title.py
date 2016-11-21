# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0024_auto_20161121_2231'),
    ]

    operations = [
        migrations.AddField(
            model_name='cardtext',
            name='title',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
