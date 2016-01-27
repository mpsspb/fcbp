# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0016_discount_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='discount',
            name='value',
        ),
        migrations.AlterField(
            model_name='discount',
            name='description',
            field=models.CharField(unique=True, max_length=150),
        ),
    ]
