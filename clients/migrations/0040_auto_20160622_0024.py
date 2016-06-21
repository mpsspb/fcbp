# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0039_freezeticket_prolongationticket'),
    ]

    operations = [
        migrations.AddField(
            model_name='clientticket',
            name='block_comment',
            field=models.CharField(max_length=150, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='clientticket',
            name='printed',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
