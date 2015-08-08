# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('patronymic', models.CharField(max_length=30)),
                ('born', models.DateField()),
                ('gender', models.SmallIntegerField(default=0, blank=True)),
                ('mobile', models.BigIntegerField(null=True, blank=True)),
                ('address', models.CharField(max_length=100, null=True, blank=True)),
                ('passport', models.TextField(null=True, blank=True)),
                ('phone', models.IntegerField(null=True, blank=True)),
                ('email', models.EmailField(max_length=75, null=True, blank=True)),
                ('avatar', models.ImageField(upload_to=b'avatar/', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
