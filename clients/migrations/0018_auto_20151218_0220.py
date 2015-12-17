# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0017_auto_20151218_0051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fitnessclubcard',
            name='personal',
            field=models.ForeignKey(to='employees.Employee'),
        ),
    ]
