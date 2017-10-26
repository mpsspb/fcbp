# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0057_useclientpersonal_club_card_visit'),
    ]

    operations = [
        migrations.AddField(
            model_name='clientpersonal',
            name='block_comment',
            field=models.CharField(max_length=150, null=True, blank=True),
            preserve_default=True,
        ),
    ]
