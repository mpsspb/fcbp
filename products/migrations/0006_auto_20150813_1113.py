# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_period_is_month'),
    ]

    operations = [
        migrations.AddField(
            model_name='clubcard',
            name='clients_count',
            field=models.IntegerField(default=1, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='clubcard',
            name='period_prolongation',
            field=models.IntegerField(default=0, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='clubcard',
            name='freeze_times',
            field=models.IntegerField(default=0, blank=True),
        ),
        migrations.AlterField(
            model_name='clubcard',
            name='guest_training',
            field=models.SmallIntegerField(default=0, blank=True),
        ),
        migrations.AlterField(
            model_name='clubcard',
            name='period_activation',
            field=models.IntegerField(default=0, blank=True),
        ),
        migrations.AlterField(
            model_name='clubcard',
            name='period_freeze',
            field=models.IntegerField(default=0, blank=True),
        ),
    ]
