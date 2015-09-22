# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0010_credit_is_credit'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='credit',
            name='aqua_aerobics',
        ),
        migrations.RemoveField(
            model_name='credit',
            name='club_card',
        ),
        migrations.RemoveField(
            model_name='credit',
            name='personal',
        ),
        migrations.RemoveField(
            model_name='credit',
            name='ticket',
        ),
        migrations.RemoveField(
            model_name='credit',
            name='timing',
        ),
        migrations.RemoveField(
            model_name='payment',
            name='aqua_aerobics',
        ),
        migrations.RemoveField(
            model_name='payment',
            name='club_card',
        ),
        migrations.RemoveField(
            model_name='payment',
            name='personal',
        ),
        migrations.RemoveField(
            model_name='payment',
            name='ticket',
        ),
        migrations.RemoveField(
            model_name='payment',
            name='timing',
        ),
    ]
