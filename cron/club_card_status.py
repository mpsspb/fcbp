#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
from datetime import date, timedelta

# import argparse
import django
from django.conf import settings
# Add extra path for the script
sys.path += ['.', '..']

# The project settings module
os.environ['DJANGO_SETTINGS_MODULE'] = 'fcbp.settings'
django.setup()


from clients.models import ClientClubCard, ClientAquaAerobics, date_end


def activate_card(**kwargs):
    """
    Reminder if balance not enough for auto prolongation.
    """
    for card in ClientClubCard.objects.filter(
            date_begin__isnull=True, is_paid_activate=False):
        # period for activate
        days = card.club_card.period_activation
        if card.date_start + timedelta(days) < date.today():
            card.date_begin = date.today()
            card.date_end = date_end(date.today(), card.club_card)
            card.save()


def end_card(**kwargs):
    """
    Disable client club card.
    """
    expire = ClientClubCard.objects.filter(
        date_end__lt=date.today()).exclude(status=0)
    for card in expire:
        card.deactivate()


if __name__ == '__main__':
    end_card()
    activate_card()
