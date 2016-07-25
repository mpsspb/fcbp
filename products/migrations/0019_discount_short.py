# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0018_training'),
    ]

    operations = [
        migrations.AddField(
            model_name='discount',
            name='short',
            field=models.CharField(max_length=3, unique=True, null=True, blank=True),
            preserve_default=True,
        ),
    ]
