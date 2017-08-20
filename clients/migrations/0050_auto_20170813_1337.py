# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0004_employee_is_active'),
        ('clients', '0049_auto_20170726_0024'),
    ]

    operations = [
        migrations.AddField(
            model_name='clientpersonal',
            name='instructor',
            field=models.ForeignKey(blank=True, to='employees.Employee', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='useclientpersonal',
            name='client_personal',
            field=models.ForeignKey(related_name=b'visits', to='clients.ClientPersonal'),
        ),
    ]
