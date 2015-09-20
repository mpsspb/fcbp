from django.db import models

from products.models import ClubCard, AquaAerobics, Sport, Ticket, Personal
from products.models import Timing
from clients.models import Client


class Debt(models.Model):
    """
    Database view clients credits before payment,
    with schedule less today.

    """
    date = models.DateTimeField(auto_now_add=True)
    schedule = models.DateField(blank=True, null=True)
    amount = models.FloatField()
    count = models.IntegerField(default=1, blank=True)
    client = models.ForeignKey(Client, blank=True, null=True)
    club_card = models.ForeignKey(ClubCard, blank=True, null=True)
    aqua_aerobics = models.ForeignKey(AquaAerobics, blank=True, null=True)
    ticket = models.ForeignKey(Ticket, blank=True, null=True)
    personal = models.ForeignKey(Personal, blank=True, null=True)
    timing = models.ForeignKey(Timing, blank=True, null=True)
    discount = models.IntegerField(default=0)
    is_credit = models.BooleanField(default=False)
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        db_table = 'v_client_debt'
        managed = False


class DebtUpcoming(models.Model):
    """
    Database view clients credits before payment,
    with schedule less today plus 7 days.

    """
    date = models.DateTimeField(auto_now_add=True)
    schedule = models.DateField(blank=True, null=True)
    amount = models.FloatField()
    count = models.IntegerField(default=1, blank=True)
    client = models.ForeignKey(Client, blank=True, null=True)
    club_card = models.ForeignKey(ClubCard, blank=True, null=True)
    aqua_aerobics = models.ForeignKey(AquaAerobics, blank=True, null=True)
    ticket = models.ForeignKey(Ticket, blank=True, null=True)
    personal = models.ForeignKey(Personal, blank=True, null=True)
    timing = models.ForeignKey(Timing, blank=True, null=True)
    discount = models.IntegerField(default=0)
    is_credit = models.BooleanField(default=False)
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        db_table = 'v_client_debt_upcoming'
        managed = False
