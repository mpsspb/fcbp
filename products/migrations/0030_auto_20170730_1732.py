# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0029_personal_club_card_only'),
    ]

    operations = [
        migrations.AddField(
            model_name='personal',
            name='short_name',
            field=models.CharField(default='', max_length=20, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='personalposition',
            name='personal',
            field=models.ForeignKey(related_name='positions', blank=True, to='products.Personal', null=True),
        ),
    ]
