# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0002_auto_20150810_1455'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='avatar',
            field=models.ImageField(null=True, upload_to=b'avatar/', blank=True),
        ),
    ]
