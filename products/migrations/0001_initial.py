# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClubCard',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=255)),
                ('max_visit', models.IntegerField()),
                ('is_full_time', models.BooleanField(default=True)),
                ('is_active', models.BooleanField(default=True)),
                ('period_freeze', models.IntegerField(default=0)),
                ('period_activation', models.IntegerField(default=0)),
                ('guest_training', models.SmallIntegerField(default=0)),
                ('fitness_testing_discount', models.BooleanField(default=False)),
                ('personal_training', models.BooleanField(default=False)),
                ('price', models.DecimalField(max_digits=15, decimal_places=2)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Discount',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('value', models.SmallIntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Period',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('value', models.SmallIntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='clubcard',
            name='period',
            field=models.ForeignKey(to='products.Period'),
            preserve_default=True,
        ),
    ]
