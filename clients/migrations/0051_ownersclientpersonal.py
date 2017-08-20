# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import clients.models.generic


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0050_auto_20170813_1337'),
    ]

    operations = [
        migrations.CreateModel(
            name='OwnersClientPersonal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('client', models.ForeignKey(related_name=b'+', to='clients.Client')),
                ('personal', models.ForeignKey(related_name=b'owners', to='clients.ClientPersonal')),
            ],
            options={
            },
            bases=(clients.models.generic.WritePayment, models.Model),
        ),
    ]
