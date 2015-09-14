# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0004_clientaquaaerobics_clientclubcard_clientpersonal_clientticket_clienttiming'),
    ]

    operations = [
        migrations.CreateModel(
            name='UseClientAquaAerobics',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('end', models.DateField(null=True, blank=True)),
                ('client_aqua_aerobics', models.ForeignKey(to='clients.ClientAquaAerobics')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UseClientClubCard',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('end', models.DateField(null=True, blank=True)),
                ('client_club_card', models.ForeignKey(to='clients.ClientClubCard')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UseClientPersonal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('end', models.DateField(null=True, blank=True)),
                ('client_personal', models.ForeignKey(to='clients.ClientPersonal')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UseClientTicket',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('end', models.DateField(null=True, blank=True)),
                ('client_ticket', models.ForeignKey(to='clients.ClientTicket')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UseClientTiming',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('end', models.DateField(null=True, blank=True)),
                ('minutes', models.IntegerField(default=1, blank=True)),
                ('client_timing', models.ForeignKey(to='clients.ClientTiming')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
