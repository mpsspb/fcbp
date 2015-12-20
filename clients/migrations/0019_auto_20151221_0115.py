# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0018_auto_20151218_0220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useclientaquaaerobics',
            name='end',
            field=models.DateTimeField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='useclientclubcard',
            name='end',
            field=models.DateTimeField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='useclientpersonal',
            name='end',
            field=models.DateTimeField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='useclientticket',
            name='end',
            field=models.DateTimeField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='useclienttiming',
            name='end',
            field=models.DateTimeField(null=True, blank=True),
        ),
    ]
