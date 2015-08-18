# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0011_auto_20150816_0118'),
    ]

    operations = [
        migrations.CreateModel(
            name='tPersonalPosition',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('position', models.CharField(max_length=255)),
                ('personal', models.ForeignKey(blank=True, to='products.Personal', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='vPersonalPosition',
            fields=[
            ],
            options={
                'db_table': 'v_personal_position',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='personalposition',
            name='personal',
            field=models.ForeignKey(blank=True, to='products.Personal', null=True),
        ),
        migrations.AlterField(
            model_name='personalposition',
            name='position',
            field=models.ForeignKey(to='employees.Position', blank=True),
        ),
    ]
