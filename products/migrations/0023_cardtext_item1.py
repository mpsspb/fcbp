# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0022_auto_20160818_0023'),
    ]

    operations = [
        migrations.AddField(
            model_name='cardtext',
            name='item1',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
