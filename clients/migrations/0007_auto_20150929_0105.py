# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0006_auto_20150924_0127'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClientOnline',
            fields=[
            ],
            options={
                'db_table': 'v_client_online',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='client',
            name='card',
            field=models.BigIntegerField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
