# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0030_clientclubcard_employee'),
    ]

    operations = [
        migrations.AddField(
            model_name='clientclubcard',
            name='printed',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
