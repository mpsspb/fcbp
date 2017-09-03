# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0004_employee_is_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeeposition',
            name='employee',
            field=models.ForeignKey(related_name=b'positions', to='employees.Employee'),
        ),
    ]
