# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0036_auto_20160531_0021'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProlongationAqua',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField()),
                ('days', models.SmallIntegerField()),
                ('amount', models.DecimalField(max_digits=15, decimal_places=2)),
                ('is_paid', models.BooleanField(default=False)),
                ('client_aqua', models.ForeignKey(to='clients.ClientAquaAerobics')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
