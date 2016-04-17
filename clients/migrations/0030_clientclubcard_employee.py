# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0003_employee_is_seller'),
        ('clients', '0029_clientclubcard_block_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='clientclubcard',
            name='employee',
            field=models.ForeignKey(blank=True, to='employees.Employee', null=True),
            preserve_default=True,
        ),
    ]
