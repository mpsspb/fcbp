# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0012_auto_20150921_0208'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='credit',
            options={'ordering': ('schedule',)},
        ),
    ]
