# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0013_auto_20150819_0102'),
        ('clients', '0003_auto_20150812_1736'),
    ]

    operations = [
        migrations.CreateModel(
            name='Credit',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('amount', models.FloatField(validators=[django.core.validators.MinValueValidator(0)])),
                ('count', models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(0)])),
                ('aqua_aerobics', models.ForeignKey(blank=True, to='products.AquaAerobics', null=True)),
                ('client', models.ForeignKey(blank=True, to='clients.Client', null=True)),
                ('club_card', models.ForeignKey(blank=True, to='products.ClubCard', null=True)),
                ('personal', models.ForeignKey(blank=True, to='products.Personal', null=True)),
                ('sport', models.ForeignKey(blank=True, to='products.Sport', null=True)),
                ('ticket', models.ForeignKey(blank=True, to='products.Ticket', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
