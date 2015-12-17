# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0016_freezeclubcard_is_paid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personalclubcard',
            name='personal',
            field=models.ForeignKey(to='employees.Employee'),
        ),
    ]
