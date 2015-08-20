from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from products.models import ClubCard, AquaAerobics, Sport, Ticket, Personal
from clients.models import Client


class Credit(models.Model):
    """
    Clients credits before payment.

    """
    date = models.DateTimeField(auto_now_add=True)
    amount = models.FloatField(validators=[MinValueValidator(0),])
    count = models.IntegerField(default=1, validators=[MinValueValidator(0),])
    client = models.ForeignKey(Client, blank=True, null=True)
    club_card = models.ForeignKey(ClubCard, blank=True, null=True)
    aqua_aerobics = models.ForeignKey(AquaAerobics, blank=True, null=True)
    ticket = models.ForeignKey(Ticket, blank=True, null=True)
    personal = models.ForeignKey(Personal, blank=True, null=True)
    discount = models.IntegerField(default=0,
                                   validators=[MinValueValidator(0),
                                               MaxValueValidator(100)])
