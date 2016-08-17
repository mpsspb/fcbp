# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0021_cardtextitems_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cardtext',
            name='text_type',
            field=models.SmallIntegerField(unique=True, choices=[(1, '\u043a\u043b\u0443\u0431\u043d\u0430\u044f \u043a\u0430\u0440\u0442\u0430')]),
        ),
    ]
