# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0020_cardtext_cardtextitems'),
    ]

    operations = [
        migrations.AddField(
            model_name='cardtextitems',
            name='date',
            field=models.DateTimeField(default=datetime.date(2016, 7, 26), auto_now_add=True),
            preserve_default=False,
        ),
    ]
