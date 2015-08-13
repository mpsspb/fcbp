# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_auto_20150813_1113'),
    ]

    operations = [
        migrations.CreateModel(
            name='AquaAerobics',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=255)),
                ('max_visit', models.IntegerField()),
                ('is_full_time', models.BooleanField(default=True)),
                ('is_active', models.BooleanField(default=True)),
                ('clients_count', models.IntegerField(default=1, blank=True)),
                ('period_prolongation', models.IntegerField(default=0, blank=True)),
                ('price', models.DecimalField(max_digits=15, decimal_places=2)),
                ('period', models.ForeignKey(to='products.Period')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
