# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0034_auto_20160525_2358'),
    ]

    operations = [
        migrations.CreateModel(
            name='FreezeAqua',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('fdate', models.DateField()),
                ('days', models.SmallIntegerField()),
                ('is_paid', models.BooleanField(default=False)),
                ('amount', models.IntegerField(null=True, blank=True)),
                ('client_aqua', models.ForeignKey(to='clients.ClientAquaAerobics')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
