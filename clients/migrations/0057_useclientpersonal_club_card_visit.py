# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0056_auto_20171022_2106'),
    ]

    operations = [
        migrations.AddField(
            model_name='useclientpersonal',
            name='club_card_visit',
            field=models.ForeignKey(blank=True, to='clients.UseClientClubCard', null=True),
            preserve_default=True,
        ),
    ]
