# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0040_auto_20160622_0024'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientticket',
            name='date_begin',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='clientticket',
            name='date_end',
            field=models.DateField(null=True, blank=True),
        ),
    ]
