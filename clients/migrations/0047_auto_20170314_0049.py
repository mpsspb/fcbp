# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0046_auto_20170123_2345'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useclientclubcard',
            name='client_club_card',
            field=models.ForeignKey(related_name=b'visits', to='clients.ClientClubCard'),
        ),
    ]
