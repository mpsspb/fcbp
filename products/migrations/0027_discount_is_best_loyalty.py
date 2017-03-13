# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0026_clubcard_short_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='discount',
            name='is_best_loyalty',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
