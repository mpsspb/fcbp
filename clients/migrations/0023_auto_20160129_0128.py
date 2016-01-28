# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0022_clientclubcard_discount'),
    ]

    operations = [
        migrations.RenameField(
            model_name='clientclubcard',
            old_name='discount',
            new_name='discount_type',
        ),
    ]
