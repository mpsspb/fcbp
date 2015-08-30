# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0007_credit_planedate'),
    ]

    operations = [
        migrations.RenameField(
            model_name='credit',
            old_name='planedate',
            new_name='schedule',
        ),
    ]
