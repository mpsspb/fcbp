# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0010_fitnessclubcard_personalclubcard'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProlongationClubCard',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('days', models.SmallIntegerField()),
                ('amount', models.DecimalField(max_digits=15, decimal_places=2)),
                ('is_paid', models.BooleanField(default=False)),
                ('client_club_card', models.ForeignKey(to='clients.ClientClubCard')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
