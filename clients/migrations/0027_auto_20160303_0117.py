# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0026_auto_20160302_0137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientclubcard',
            name='date_begin',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='clientclubcard',
            name='date_end',
            field=models.DateField(null=True, blank=True),
        ),
    ]
