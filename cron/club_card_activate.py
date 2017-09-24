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


from clients.models import ClientClubCard, ClientPersonal


def activate_card(**kwargs):
    """
    Reminder if balance not enough for auto prolongation.
    """
    for card in ClientClubCard.objects.filter(
            date_begin__isnull=True, is_paid_activate=False):
        # period for activate
        days = card.club_card.period_activation
        if card.date_start + timedelta(days - 1) < date.today():
            card.activate()


def activate_personal(**kwargs):
    """
    Reminder if balance not enough for auto prolongation.
    """
    for card in ClientPersonal.objects.filter(date_begin__isnull=True):
        # period for activate
        days = card.personal.period_activation
        if card.date_start + timedelta(days - 1) < date.today():
            card.activate()


if __name__ == '__main__':
    activate_card()
    activate_personal()
