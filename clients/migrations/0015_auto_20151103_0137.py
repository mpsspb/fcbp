# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0014_auto_20151102_0135'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClientAquaAerobicsFull',
            fields=[
            ],
            options={
                'db_table': 'v_external_aqua',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='guestclubcard',
            name='phone',
            field=models.BigIntegerField(null=True, blank=True),
        ),
    ]
