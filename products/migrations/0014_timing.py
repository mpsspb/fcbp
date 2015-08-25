# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0013_auto_20150819_0102'),
    ]

    operations = [
        migrations.CreateModel(
            name='Timing',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=255)),
                ('price', models.DecimalField(max_digits=15, decimal_places=2)),
                ('period_prolongation', models.IntegerField(default=0, blank=True)),
                ('clients_count', models.IntegerField(default=1, blank=True)),
                ('minutes', models.IntegerField(default=1, blank=True)),
                ('period_freeze', models.IntegerField(default=0, blank=True)),
                ('is_active', models.BooleanField(default=True)),
                ('period', models.ForeignKey(to='products.Period')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
