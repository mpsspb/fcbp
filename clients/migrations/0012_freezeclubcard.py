# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0011_prolongationclubcard'),
    ]

    operations = [
        migrations.CreateModel(
            name='FreezeClubCard',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('fdate', models.DateTimeField()),
                ('days', models.SmallIntegerField()),
                ('client_club_card', models.ForeignKey(to='clients.ClientClubCard')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
