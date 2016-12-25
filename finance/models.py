# -*- coding: utf-8 -*-
from datetime import datetime

from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.translation import ugettext as _

from clients.models import ClientClubCard, ClientAquaAerobics, ClientTicket
from clients.models import Client, ClientPersonal, ClientTiming


class Credit(models.Model):

    """
    Clients credits before payment.

    """
    date = models.DateTimeField(auto_now_add=True)
    schedule = models.DateField(blank=True, null=True)
    amount = models.FloatField(validators=[MinValueValidator(0), ])
    count = models.IntegerField(default=1, blank=True,
                                validators=[MinValueValidator(1), ])
    client = models.ForeignKey(Client, blank=True, null=True)
    club_card = models.ForeignKey(ClientClubCard, blank=True, null=True)
    aqua_aerobics = models.ForeignKey(ClientAquaAerobics, blank=True,
                                      null=True)
    ticket = models.ForeignKey(ClientTicket, blank=True, null=True)
    personal = models.ForeignKey(ClientPersonal, blank=True, null=True)
    timing = models.ForeignKey(ClientTiming, blank=True, null=True)
    discount = models.IntegerField(default=0,
                                   validators=[MinValueValidator(0),
                                               MaxValueValidator(100)])
    is_credit = models.BooleanField(default=False)

    class Meta:
        ordering = ('schedule',)

    def split(self, amount):
        try:
            amount = int(amount)
        except Exception as e:
            return
        new_credit = self
        new_credit.amount = self.amount - amount
        new_credit.pk = None
        new_credit.save()


class Payment(models.Model):

    payment_types = {
        1: _('cash'),
        2: _('cashless'),
        3: _('bank'),
        0: _('other')
    }
    """
    Client payments.
    """
    date = models.DateTimeField(blank=True)
    payment_type = models.SmallIntegerField(default=1, )
    amount = models.FloatField(validators=[MinValueValidator(0), ])
    count = models.IntegerField(default=1,
                                validators=[MinValueValidator(0), ])
    client = models.ForeignKey(Client, blank=True, null=True)
    credit = models.ForeignKey(Credit, blank=True, null=True)
    club_card = models.ForeignKey(ClientClubCard, blank=True, null=True)
    aqua_aerobics = models.ForeignKey(ClientAquaAerobics, blank=True,
                                      null=True)
    ticket = models.ForeignKey(ClientTicket, blank=True, null=True)
    personal = models.ForeignKey(ClientPersonal, blank=True, null=True)
    timing = models.ForeignKey(ClientTiming, blank=True, null=True)
    discount = models.IntegerField(default=0,
                                   validators=[MinValueValidator(0),
                                               MaxValueValidator(100)])

    def save(self, *args, **kwargs):
        if not self.date:
            self.date = datetime.now()
        super(Payment, self).save(*args, **kwargs)

    def goods(self):
        # first of existing goods
        all_goods = (
            self.club_card, self.aqua_aerobics, self.ticket, self.personal,
            self.timing)
        return next(x for x in all_goods if x)

    def description(self):
        msg = u'Платеж от {date} на сумму {amount} руб. за {goods}'
        data = {'date': self.date, 'amount': self.amount,
                'goods': self.goods().name}
        return msg.format(**data)

    def split(self, amount):
        try:
            amount = int(amount)
        except Exception as e:
            return
        new_payment = self
        new_payment.amount = self.amount - amount
        new_payment.pk = None
        new_payment.save()
