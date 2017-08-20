# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import clients.models.generic


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0051_ownersclientpersonal'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProlongationPersonal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField()),
                ('days', models.SmallIntegerField()),
                ('amount', models.DecimalField(max_digits=15, decimal_places=2)),
                ('is_paid', models.BooleanField(default=False)),
                ('is_extra', models.BooleanField(default=False)),
                ('note', models.TextField(null=True, blank=True)),
                ('personal', models.ForeignKey(related_name=b'prolongation', to='clients.ClientPersonal')),
            ],
            options={
            },
            bases=(clients.models.generic.Prolongation, clients.models.generic.WritePayment, models.Model),
        ),
    ]
