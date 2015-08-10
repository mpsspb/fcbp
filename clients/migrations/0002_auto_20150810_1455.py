# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='date',
            field=models.DateTimeField(default=datetime.date(2015, 8, 10), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='client',
            name='uid',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
