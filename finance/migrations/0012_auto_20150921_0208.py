# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0005_useclientaquaaerobics_useclientclubcard_useclientpersonal_useclientticket_useclienttiming'),
        ('finance', '0011_auto_20150921_0208'),
    ]

    operations = [
        migrations.AddField(
            model_name='credit',
            name='aqua_aerobics',
            field=models.ForeignKey(blank=True, to='clients.ClientAquaAerobics', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='credit',
            name='club_card',
            field=models.ForeignKey(blank=True, to='clients.ClientClubCard', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='credit',
            name='personal',
            field=models.ForeignKey(blank=True, to='clients.ClientPersonal', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='credit',
            name='ticket',
            field=models.ForeignKey(blank=True, to='clients.ClientTicket', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='credit',
            name='timing',
            field=models.ForeignKey(blank=True, to='clients.ClientTiming', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='payment',
            name='aqua_aerobics',
            field=models.ForeignKey(blank=True, to='clients.ClientAquaAerobics', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='payment',
            name='club_card',
            field=models.ForeignKey(blank=True, to='clients.ClientClubCard', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='payment',
            name='personal',
            field=models.ForeignKey(blank=True, to='clients.ClientPersonal', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='payment',
            name='ticket',
            field=models.ForeignKey(blank=True, to='clients.ClientTicket', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='payment',
            name='timing',
            field=models.ForeignKey(blank=True, to='clients.ClientTiming', null=True),
            preserve_default=True,
        ),
    ]
