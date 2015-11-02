# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0013_auto_20151012_0255'),
    ]

    operations = [
        migrations.CreateModel(
            name='AquaAerobicsClients',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('client', models.ForeignKey(to='clients.Client')),
                ('client_aqua', models.ForeignKey(to='clients.ClientAquaAerobics')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='aquaaerobicsclients',
            unique_together=set([('client', 'client_aqua')]),
        ),
    ]
