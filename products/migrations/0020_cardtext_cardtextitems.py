# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0019_discount_short'),
    ]

    operations = [
        migrations.CreateModel(
            name='CardText',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text_type', models.SmallIntegerField(unique=True, choices=[(1, b'\xd0\xba\xd0\xbb\xd1\x83\xd0\xb1\xd0\xbd\xd0\xb0\xd1\x8f \xd0\xba\xd0\xb0\xd1\x80\xd1\x82\xd0\xb0')])),
                ('header', models.TextField(null=True, blank=True)),
                ('additional_header', models.TextField(null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CardTextItems',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('item', models.TextField()),
                ('order', models.SmallIntegerField()),
                ('card_text', models.ForeignKey(to='products.CardText')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
