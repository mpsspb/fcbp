# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_aquaaerobics'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sport',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=255)),
                ('is_full_time', models.BooleanField(default=True)),
                ('max_visit', models.IntegerField()),
                ('period_prolongation', models.IntegerField(default=0, blank=True)),
                ('period', models.ForeignKey(to='products.Period')),
                ('sport', models.ForeignKey(to='products.Sport')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
