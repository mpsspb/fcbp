# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0003_employee_is_seller'),
        ('clients', '0032_auto_20160525_0008'),
    ]

    operations = [
        migrations.AddField(
            model_name='clientaquaaerobics',
            name='employee',
            field=models.ForeignKey(blank=True, to='employees.Employee', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='clientaquaaerobics',
            name='printed',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
