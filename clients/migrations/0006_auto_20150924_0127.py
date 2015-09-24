# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0002_employee_employeeposition'),
        ('clients', '0005_useclientaquaaerobics_useclientclubcard_useclientpersonal_useclientticket_useclienttiming'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='introductory_date',
            field=models.DateTimeField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='client',
            name='introductory_employee',
            field=models.ForeignKey(blank=True, to='employees.Employee', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='clientaquaaerobics',
            name='date_begin',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='clientaquaaerobics',
            name='date_end',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='clientaquaaerobics',
            name='date_start',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='clientclubcard',
            name='date_begin',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='clientclubcard',
            name='date_end',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='clientclubcard',
            name='date_start',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='clientpersonal',
            name='date_begin',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='clientpersonal',
            name='date_end',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='clientpersonal',
            name='date_start',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='clientticket',
            name='date_begin',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='clientticket',
            name='date_end',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='clientticket',
            name='date_start',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='clienttiming',
            name='date_begin',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='clienttiming',
            name='date_end',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='clienttiming',
            name='date_start',
            field=models.DateField(blank=True),
        ),
    ]
