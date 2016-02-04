# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0018_training'),
        ('clients', '0024_clientclubcard_discount_amount'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClubCardTrains',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('training', models.ForeignKey(to='products.Training')),
                ('visit', models.ForeignKey(to='clients.UseClientClubCard')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
