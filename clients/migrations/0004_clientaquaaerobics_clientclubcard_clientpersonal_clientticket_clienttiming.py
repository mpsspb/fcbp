# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0014_timing'),
        ('clients', '0003_auto_20150812_1736'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClientAquaAerobics',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('date_start', models.DateField()),
                ('date_begin', models.DateField()),
                ('date_end', models.DateField()),
                ('status', models.SmallIntegerField(default=2, blank=True)),
                ('aqua_aerobics', models.ForeignKey(to='products.AquaAerobics')),
                ('client', models.ForeignKey(to='clients.Client')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ClientClubCard',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('date_start', models.DateField()),
                ('date_begin', models.DateField()),
                ('date_end', models.DateField()),
                ('status', models.SmallIntegerField(default=2, blank=True)),
                ('client', models.ForeignKey(to='clients.Client')),
                ('club_card', models.ForeignKey(to='products.ClubCard')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ClientPersonal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('date_start', models.DateField()),
                ('date_begin', models.DateField()),
                ('date_end', models.DateField()),
                ('status', models.SmallIntegerField(default=2, blank=True)),
                ('client', models.ForeignKey(to='clients.Client')),
                ('personal', models.ForeignKey(to='products.Personal')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ClientTicket',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('date_start', models.DateField()),
                ('date_begin', models.DateField()),
                ('date_end', models.DateField()),
                ('status', models.SmallIntegerField(default=2, blank=True)),
                ('client', models.ForeignKey(to='clients.Client')),
                ('ticket', models.ForeignKey(to='products.Ticket')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ClientTiming',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('date_start', models.DateField()),
                ('date_begin', models.DateField()),
                ('date_end', models.DateField()),
                ('status', models.SmallIntegerField(default=2, blank=True)),
                ('client', models.ForeignKey(to='clients.Client')),
                ('timing', models.ForeignKey(to='products.Timing')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
