# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0054_auto_20170904_0135'),
    ]

    operations = [
        migrations.CreateModel(
            name='PersonalClients',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('client', models.ForeignKey(to='clients.Client')),
                ('personal', models.ForeignKey(related_name=b'extra_clients', to='clients.ClientPersonal')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='personalclients',
            unique_together=set([('client', 'personal')]),
        ),
        migrations.AlterModelOptions(
            name='useclientpersonal',
            options={'ordering': ['date']},
        ),
    ]
