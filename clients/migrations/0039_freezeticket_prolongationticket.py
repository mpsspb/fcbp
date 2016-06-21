# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import clients.models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0038_clientaquaaerobics_block_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='FreezeTicket',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('fdate', models.DateField()),
                ('days', models.SmallIntegerField()),
                ('is_paid', models.BooleanField(default=False)),
                ('amount', models.IntegerField(null=True, blank=True)),
                ('client_ticket', models.ForeignKey(to='clients.ClientTicket')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ProlongationTicket',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField()),
                ('days', models.SmallIntegerField()),
                ('amount', models.DecimalField(max_digits=15, decimal_places=2)),
                ('is_paid', models.BooleanField(default=False)),
                ('client_ticket', models.ForeignKey(to='clients.ClientTicket')),
            ],
            options={
            },
            bases=(clients.models.GenericProlongation, models.Model),
        ),
    ]
