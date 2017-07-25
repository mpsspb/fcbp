# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0048_auto_20170725_2345'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ownersclubcard',
            name='client_club_card',
        ),
        migrations.AddField(
            model_name='ownersclubcard',
            name='client',
            field=models.ForeignKey(related_name=b'+', default=1, to='clients.Client'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ownersclubcard',
            name='club_card',
            field=models.ForeignKey(related_name=b'owners', default=1, to='clients.ClientClubCard'),
            preserve_default=False,
        ),
    ]
