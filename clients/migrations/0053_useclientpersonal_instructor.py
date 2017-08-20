# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0004_employee_is_active'),
        ('clients', '0052_prolongationpersonal'),
    ]

    operations = [
        migrations.AddField(
            model_name='useclientpersonal',
            name='instructor',
            field=models.ForeignKey(blank=True, to='employees.Employee', null=True),
            preserve_default=True,
        ),
    ]
