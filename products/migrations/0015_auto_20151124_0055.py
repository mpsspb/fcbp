# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0014_timing'),
    ]

    operations = [
        migrations.AlterField(
            model_name='period',
            name='value',
            field=models.SmallIntegerField(),
        ),
        migrations.AlterUniqueTogether(
            name='period',
            unique_together=set([('value', 'is_month')]),
        ),
    ]
