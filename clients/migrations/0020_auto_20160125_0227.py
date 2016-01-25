# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0019_auto_20151221_0115'),
    ]

    operations = [
        migrations.AddField(
            model_name='freezeclubcard',
            name='amount',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='fitnessclubcard',
            name='date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='personalclubcard',
            name='date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='prolongationclubcard',
            name='date',
            field=models.DateTimeField(),
        ),
    ]
