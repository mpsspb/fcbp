# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0042_auto_20160624_0158'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='passport',
        ),
        migrations.AddField(
            model_name='client',
            name='note',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='client',
            name='passport_date',
            field=models.DateField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='client',
            name='passport_issued',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='client',
            name='passport_number',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
