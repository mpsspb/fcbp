# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0006_auto_20150829_1633'),
    ]

    operations = [
        migrations.AddField(
            model_name='credit',
            name='planedate',
            field=models.DateField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
