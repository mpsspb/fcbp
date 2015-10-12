# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0012_freezeclubcard'),
    ]

    operations = [
        migrations.AlterField(
            model_name='freezeclubcard',
            name='fdate',
            field=models.DateField(),
        ),
    ]
