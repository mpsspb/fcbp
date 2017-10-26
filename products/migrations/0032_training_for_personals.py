# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0031_personal_period_activation'),
    ]

    operations = [
        migrations.AddField(
            model_name='training',
            name='for_personals',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
