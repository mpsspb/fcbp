# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


def set_phone(apps, schema_editor):
    # set null phone to 111-222-33-44
    GuestClubCard = apps.get_model("clients", "GuestClubCard")
    for guest in GuestClubCard.objects.filter():
        guest.phone = 1112223344
        guest.save()


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0027_auto_20160303_0117'),
    ]

    operations = [
        migrations.AddField(
            model_name='guestclubcard',
            name='passport',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='guestclubcard',
            name='born',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.RunPython(set_phone),
        migrations.AlterField(
            model_name='guestclubcard',
            name='phone',
            field=models.BigIntegerField(),
        ),
    ]
