# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0002_employee_employeeposition'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='is_seller',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
