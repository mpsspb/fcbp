# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0055_auto_20170924_2259'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personalclients',
            name='client',
            field=models.ForeignKey(related_name=b'extra_personals', to='clients.Client'),
        ),
    ]
