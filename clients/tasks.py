# -*- coding: utf-8 -*-
from datetime import date, timedelta

from celery import task
from celery.schedules import crontab
from celery.decorators import periodic_task

from django.conf import settings

from .models import ClientClubCard, date_end


@periodic_task(name="clients.activate_card",
               run_every=crontab(hour=3, minute=15))
def activate_card(**kwargs):
    """
    Reminder if balance not enough for auto prolongation.
    """
    for card in ClientClubCard.objects.filter(
                                    date_begin__isnull=True,
                                    is_paid_activate=False):
        # period for activate
        days = card.club_card.period_activation
        if card.date_start + timedelta(days) < date.today():
            card.date_begin = date.today()
            card.date_end = date_end(date.today(), card.club_card)
            card.save()


@periodic_task(name="clients.end_card",
               run_every=crontab(hour=3, minute=15))
def end_card(**kwargs):
    """
    Reminder if balance not enough for auto prolongation.
    """
    for card in ClientClubCard.objects.filter(date_end__lte=date.today()):
        card.status = 0
        card.save()
