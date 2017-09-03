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


def end_card(**kwargs):
    """
    Disable client club card.
    """
    expire = ClientClubCard.objects.filter(
        date_end__lte=date.today()).exclude(status=0)
    for card in expire:
        card.deactivate()


def end_personal(**kwargs):
    """
    Disable Client Personal
    """
    expire = ClientPersonal.objects.filter(
        date_end__lte=date.today()).exclude(status=0)
    for card in expire:
        card.deactivate()


if __name__ == '__main__':
    end_card()
    end_personal()
