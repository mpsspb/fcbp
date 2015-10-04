# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0008_extclientclubcard'),
    ]

    operations = [
        migrations.CreateModel(
            name='GuestClubCard',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('guest', models.CharField(max_length=60)),
                ('born', models.DateField()),
                ('phone', models.IntegerField(null=True, blank=True)),
                ('client_club_card', models.ForeignKey(to='clients.ClientClubCard')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
