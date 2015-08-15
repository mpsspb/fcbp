# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0001_initial'),
        ('products', '0010_ticket_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Personal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=255)),
                ('max_visit', models.IntegerField()),
                ('clients_count', models.IntegerField(default=1, blank=True)),
                ('is_full_time', models.BooleanField(default=True)),
                ('is_active', models.BooleanField(default=True)),
                ('price', models.DecimalField(max_digits=15, decimal_places=2)),
                ('period_prolongation', models.IntegerField(default=0, blank=True)),
                ('period', models.ForeignKey(to='products.Period')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PersonalPosition',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('personal', models.ForeignKey(to='products.Personal')),
                ('position', models.ForeignKey(to='employees.Position')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='personalposition',
            unique_together=set([('personal', 'position')]),
        ),
    ]
