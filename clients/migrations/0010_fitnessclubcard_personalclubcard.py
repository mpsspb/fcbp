# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0014_timing'),
        ('clients', '0009_guestclubcard'),
    ]

    operations = [
        migrations.CreateModel(
            name='FitnessClubCard',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('client_club_card', models.ForeignKey(to='clients.ClientClubCard')),
                ('personal', models.ForeignKey(to='products.Personal')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PersonalClubCard',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('client_club_card', models.ForeignKey(to='clients.ClientClubCard')),
                ('personal', models.ForeignKey(to='products.Personal')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
