# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import clients.models.generic


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0047_auto_20170314_0049'),
    ]

    operations = [
        migrations.CreateModel(
            name='OwnersClubCard',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('client_club_card', models.ForeignKey(related_name=b'owners', to='clients.ClientClubCard')),
            ],
            options={
            },
            bases=(clients.models.generic.WritePayment, models.Model),
        ),
        migrations.AlterField(
            model_name='freezeclubcard',
            name='client_club_card',
            field=models.ForeignKey(related_name=b'freeze', to='clients.ClientClubCard'),
        ),
        migrations.AlterField(
            model_name='prolongationclubcard',
            name='client_club_card',
            field=models.ForeignKey(related_name=b'prolongation', to='clients.ClientClubCard'),
        ),
    ]
