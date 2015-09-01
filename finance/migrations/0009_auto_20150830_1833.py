# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0008_auto_20150830_0402'),
    ]

    operations = [
        migrations.AlterField(
            model_name='credit',
            name='count',
            field=models.IntegerField(default=1, blank=True, validators=[django.core.validators.MinValueValidator(1)]),
        ),
    ]
