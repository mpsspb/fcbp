# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0043_auto_20160722_0041'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='useclientclubcard',
            options={'ordering': ['date']},
        ),
        migrations.AlterField(
            model_name='useclientclubcard',
            name='date',
            field=models.DateTimeField(),
        ),
    ]
