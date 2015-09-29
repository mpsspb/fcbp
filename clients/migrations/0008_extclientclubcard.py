# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0007_auto_20150929_0105'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExtClientClubCard',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('client', models.ForeignKey(to='clients.Client')),
                ('client_club_card', models.ForeignKey(to='clients.ClientClubCard')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
