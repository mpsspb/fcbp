# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0025_cardtext_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='clubcard',
            name='short_name',
            field=models.CharField(default='', max_length=20, null=True, blank=True),
            preserve_default=True,
        ),
    ]
