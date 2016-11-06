# -*- coding: utf-8 -*-
import os
from datetime import date, timedelta
from dateutil.relativedelta import relativedelta

from django.db import models
from django.db.models import Sum
from django.db.models.signals import pre_save
from django.dispatch.dispatcher import receiver

from products.models import (ClubCard, AquaAerobics, Ticket, Personal, Timing,
                             Discount, Training)
from employees.models import Employee


class GenericProlongation(object):

    def parent_upd(self, *args, **kwargs):
        days = self.days
        parent = self.parent
        is_delete = kwargs.get('is_delete')
        if is_delete:
            parent.date_end = parent.date_end - timedelta(days)
        else:
            parent.date_end = parent.date_end + timedelta(days)
        parent.save()


class GenericProperty(object):

    """ Generic property need for all services """
    @property
    def client_mobile(self):
        return self.client.mobile

    @property
    def client_uid(self):
        return self.client.uid

    @property
    def client_name(self):
        return self.client.full_name

    @property
    def client_card(self):
        return self.client.card

    def escape_frozen(self):
        freeze_model = eval(self.freeze_class)
        filtr = {freeze_model.product: self, 'fdate__lte': date.today()}
        freezes = freeze_model.objects.filter(**filtr)
        for f in freezes:
            if f.tdate >= date.today():
                days_freeze = (date.today() - f.fdate).days
                days_back = (f.tdate - date.today()).days + 1
                self.date_end = self.date_end - timedelta(days_back)
                self.save()
                f.days = days_freeze
                f.save()

    @property
    def name(self):
        return self.product.name

    def full_name(self):
        return self.product.full_name


class Client(models.Model):

    """
    Clients data.
    """
    date = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    patronymic = models.CharField(max_length=30)
    born = models.DateField()
    uid = models.IntegerField(default=0)
    card = models.BigIntegerField(blank=True, null=True)

    mobile = models.BigIntegerField(null=True, blank=True)
    gender = models.SmallIntegerField(default=0, blank=True)
    address = models.CharField(max_length=100, null=True, blank=True)
    passport_number = models.TextField(null=True, blank=True)
    passport_date = models.DateField(null=True, blank=True)
    passport_issued = models.TextField(null=True, blank=True)
    phone = models.IntegerField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    avatar = models.ImageField(upload_to="avatar/", null=True, blank=True)
    note = models.TextField(null=True, blank=True)

    introductory_date = models.DateTimeField(blank=True, null=True)
    introductory_employee = models.ForeignKey(Employee, blank=True, null=True)

    @property
    def passport(self):
        return '%s %s %s' % (
            self.passport_number, self.passport_date, self.passport_issued)

    @property
    def full_name(self,):
        return "%s %s %s" % (self.last_name, self.first_name, self.patronymic)

    @property
    def initials(self,):
        return "%s %s. %s." % (
            self.last_name, self.first_name[:1], self.patronymic[:1])

    @property
    def online_clubcard(self,):
        return ClientOnline.objects.filter(client=self, product='clubcard')\
                           .exists()

    @property
    def introductory_employee_name(self,):
        return self.introductory_employee.initials

    @property
    def online_aqua(self,):
        return ClientOnline.objects.filter(client=self, product='aqua')\
                           .exists()

    @property
    def online_ticket(self,):
        return ClientOnline.objects.filter(client=self, product='ticket')\
                           .exists()

    @property
    def online_personal(self,):
        return ClientOnline.objects.filter(client=self, product='personal')\
                           .exists()

    @property
    def avatar_url(self):
        if self.avatar:
            return self.avatar.url
        else:
            return ""

    def save(self, *args, **kwargs):
        if not self.uid:
            mon = date.today() + timedelta(days=-date.today().weekday())
            week_clients = Client.objects.filter(date__gte=mon).count()
            year = (date.today().year - 2000) * 10000
            week = date.today().isocalendar()[1] * 100
            cnt = week_clients + 1
            self.uid = year + week + cnt
            self.first_name = self.first_name.strip()
            self.last_name = self.last_name.strip()
            self.patronymic = self.patronymic.strip()
        super(Client, self).save(*args, **kwargs)


@receiver(pre_save, sender=Client)
def auto_delete_file_on_change(sender, instance, **kwargs):
    """Deletes file from filesystem
    when corresponding `Client` object is changed.
    """
    if not instance.pk:
        return False
    try:
        old_file = Client.objects.get(pk=instance.pk).avatar
    except Client.DoesNotExist:
        return False

    new_file = instance.avatar
    if not old_file == new_file:
        if os.path.isfile(old_file.path):
            os.remove(old_file.path)


class ClientClubCard(GenericProperty, models.Model):

    """
    The clients club card,
    history and status.

    Date start - the date for the start period of activation.
    Date begin - is start of using the card.

    """
    freeze_class = 'FreezeClubCard'

    date = models.DateTimeField(auto_now_add=True)
    date_start = models.DateField(blank=True)
    date_begin = models.DateField(null=True, blank=True)
    date_end = models.DateField(null=True, blank=True)
    client = models.ForeignKey(Client, )
    club_card = models.ForeignKey(ClubCard, )
    is_paid_activate = models.BooleanField(default=False)
    paid_activate_amount = models.IntegerField(blank=True, null=True)
    discount_type = models.ForeignKey(Discount, blank=True, null=True)
    discount_amount = models.FloatField(blank=True, null=True)
    bonus_type = models.ForeignKey(Discount, blank=True, null=True,
                                   related_name="club_card_bonus_type")
    bonus_amount = models.FloatField(blank=True, null=True)
    block_comment = models.CharField(max_length=150, blank=True, null=True)
    status = models.SmallIntegerField(default=2, blank=True, )
    employee = models.ForeignKey(Employee, blank=True, null=True)
    printed = models.BooleanField(default=False)
    """
    status valid data:
    0 - disabled
    1 - active
    2 - prospect
    """

    def save(self, *args, **kwargs):
        if self.status == 0:
            if not self.date_begin:
                self.date_begin = date.today()
                self.date_end = date.today()
            else:
                self.date_end = date.today()
        if self.pk:
            old_date_begin = ClientClubCard.objects.get(pk=self.pk).date_begin
            if old_date_begin:
                delta_begin = None
                delta_begin = self.date_begin - old_date_begin
                if delta_begin:
                    self.date_end = date_end(self.date_begin, self.club_card)
        super(ClientClubCard, self).save(*args, **kwargs)

    def deactivate(self, ):
        self.status = 0
        self.save()

    @property
    def product(self):
        return self.club_card

    @property
    def discount_name(self):
        if self.discount_type:
            return '%s %s' % (self.discount_type.description,
                              self.discount_amount)
        else:
            return ''

    @property
    def discount_value(self):
        if self.discount_type:
            return self.discount_amount
        elif self.bonus_type:
            return self.bonus_amount
        else:
            return ''

    @property
    def discount_short(self):
        if self.discount_type:
            return self.discount_type.short
        elif self.bonus_type:
            return self.bonus_type.short
        else:
            return ''

    @property
    def discount_description(self):
        if self.discount_type:
            return self.discount_type.description
        elif self.bonus_type:
            return self.bonus_type.description
        else:
            return ''

    @property
    def period(self):
        if self.club_card.period.is_month:
            return u'%s месяцев' % self.club_card.period.value
        else:
            return u'%s дней' % self.club_card.period.value

    @property
    def personal_training(self):
        if self.club_card.personal_training:
            return 1
        else:
            return 0

    @property
    def rest_days(self):
        if not self.date_end:
            return None
        rest_days = (self.date_end - date.today()).days
        if rest_days < 1:
            return 0
        return rest_days

    @property
    def rest_visits(self):
        if self.club_card.max_visit == 99999:
            return '-'
        visits = UseClientClubCard.objects.filter(client_club_card=self)
        used = ClubCardTrains.objects.filter(visit__in=visits).count()
        return self.club_card.max_visit - used

    @property
    def rest_visits_int(self):
        if self.club_card.max_visit == 99999:
            return 99999
        visits = UseClientClubCard.objects.filter(client_club_card=self)
        used = ClubCardTrains.objects.filter(visit__in=visits).count()
        return self.club_card.max_visit - used

    @property
    def is_online(self):
        return UseClientClubCard.objects.filter(client_club_card=self,
                                                end__isnull=True).count()

    @property
    def rest_guest(self):
        guests = GuestClubCard.objects\
                              .filter(client_club_card=self).count()
        return self.club_card.guest_training - guests

    @property
    def rest_freeze(self):
        freeze = FreezeClubCard.objects\
                               .filter(client_club_card=self)\
                               .aggregate(sum=Sum('days'))
        if freeze['sum']:
            return self.club_card.period_freeze - freeze['sum']
        return self.club_card.period_freeze

    @property
    def rest_freeze_times(self):
        times = FreezeClubCard.objects\
                              .filter(client_club_card=self).count()
        return self.club_card.freeze_times - times

    @property
    def guest_training(self):
        return self.club_card.guest_training

    @property
    def fitness_testing_discount(self):
        if FitnessClubCard.objects.filter(client_club_card=self).exists():
            return False
        return self.club_card.fitness_testing_discount

    @property
    def personal_training(self):
        if PersonalClubCard.objects.filter(client_club_card=self).exists():
            return False
        return self.club_card.personal_training

    @property
    def is_frozen(self):
        freezes = FreezeClubCard.objects\
                                .filter(client_club_card=self,
                                        fdate__lte=date.today())
        for f in freezes:
            if f.tdate >= date.today():
                return True

        return False


class ProlongationClubCard(GenericProlongation, models.Model):

    """
    Prolongation for the Client Club Card.
    """
    date = models.DateTimeField()
    client_club_card = models.ForeignKey(ClientClubCard)
    days = models.SmallIntegerField()
    amount = models.DecimalField(max_digits=15, decimal_places=2,)
    is_paid = models.BooleanField(default=False)

    @property
    def parent(self):
        return self.client_club_card

    def save(self, *args, **kwargs):
        if not self.pk:
            self.parent_upd(self,)
        super(ProlongationClubCard, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        self.parent_upd(self, is_delete=True)
        super(ProlongationClubCard, self).delete(*args, **kwargs)


class GuestClubCard(models.Model):

    """
    Guest training for the Client Club Card.
    """
    date = models.DateTimeField(auto_now_add=True)
    client_club_card = models.ForeignKey(ClientClubCard)
    guest = models.CharField(max_length=60)
    phone = models.BigIntegerField()
    born = models.DateField(null=True, blank=True)
    passport = models.TextField(null=True, blank=True)


class FitnessClubCard(models.Model):

    """
    Fitness  testing discount for the Client Club Card.
    """
    date = models.DateTimeField()
    client_club_card = models.ForeignKey(ClientClubCard)
    personal = models.ForeignKey(Employee, )

    def save(self, *args, **kwargs):
        if not self.pk:
            card = self.client_club_card
            if not card.date_begin:
                card.date_begin = date.today()
                card.date_end = date_end(date.today(), card.club_card)
                card.save()
        super(FitnessClubCard, self).save(*args, **kwargs)

    @property
    def employee(self):
        return self.personal.initials


class PersonalClubCard(models.Model):

    """
    Personal training discount for the Client Club Card.
    """
    date = models.DateTimeField()
    client_club_card = models.ForeignKey(ClientClubCard)
    personal = models.ForeignKey(Employee)

    @property
    def employee(self):
        return self.personal.initials


class FreezeClubCard(models.Model):

    """
    Freeze club card.
    """
    product = 'client_club_card'

    date = models.DateTimeField(auto_now_add=True)
    client_club_card = models.ForeignKey(ClientClubCard)
    fdate = models.DateField()
    days = models.SmallIntegerField()
    is_paid = models.BooleanField(default=False)
    amount = models.IntegerField(blank=True, null=True)

    @property
    def tdate(self):
        return self.fdate + timedelta(days=(self.days-1))

    def delete(self, *args, **kwargs):
        cc = self.client_club_card
        cc.date_end = cc.date_end - timedelta(days=self.days)
        cc.save()
        super(FreezeClubCard, self).delete(*args, **kwargs)


class ClientAquaAerobics(GenericProperty, models.Model):

    """
    The clients Aqua Aerobics card,
    history and status.

    Date start - the date for the start period of activation.
    Date begin - is start of using the card.

    """

    freeze_class = 'FreezeAqua'

    date = models.DateTimeField(auto_now_add=True)
    date_start = models.DateField(blank=True)
    date_begin = models.DateField(null=True, blank=True)
    date_end = models.DateField(null=True, blank=True)
    client = models.ForeignKey(Client, )
    aqua_aerobics = models.ForeignKey(AquaAerobics, )
    discount_type = models.ForeignKey(Discount, blank=True, null=True)
    discount_amount = models.FloatField(blank=True, null=True)
    bonus_type = models.ForeignKey(Discount, blank=True, null=True,
                                   related_name="aqua_bonus_type")
    bonus_amount = models.FloatField(blank=True, null=True)
    employee = models.ForeignKey(Employee, blank=True, null=True)
    printed = models.BooleanField(default=False)
    is_paid_activate = models.BooleanField(default=False)
    paid_activate_amount = models.IntegerField(blank=True, null=True)
    block_comment = models.CharField(max_length=150, blank=True, null=True)
    status = models.SmallIntegerField(default=2, blank=True, )
    """
    status valid data:
    0 - disabled
    1 - active
    2 - prospect
    """

    @property
    def product(self):
        return self.aqua_aerobics

    @property
    def extra_client(self):
        clients = self.aquaaerobicsclients_set.all().values('client')
        return Client.objects.filter(pk__in=clients)

    @property
    def rest_days(self):
        if not self.date_end:
            return None
        rest_days = (self.date_end - date.today()).days
        if rest_days < 1:
            return 0
        return rest_days

    @property
    def rest_visits(self):
        if self.aqua_aerobics.max_visit == 99999:
            return '-'
        used = UseClientAquaAerobics.objects.filter(client_aqua_aerobics=self)\
                                            .count()
        return self.aqua_aerobics.max_visit - used

    @property
    def is_online(self):
        return UseClientAquaAerobics.objects.filter(client_aqua_aerobics=self,
                                                    end__isnull=True).count()

    @property
    def is_frozen(self):
        freezes = FreezeAqua.objects\
                            .filter(client_aqua=self,
                                    fdate__lte=date.today())
        for f in freezes:
            if f.tdate >= date.today():
                return True
        return False


class FreezeAqua(models.Model):

    """Freeze aqua aerobics."""
    product = 'client_aqua'

    date = models.DateTimeField(auto_now_add=True)
    client_aqua = models.ForeignKey(ClientAquaAerobics)
    fdate = models.DateField()
    days = models.SmallIntegerField()
    is_paid = models.BooleanField(default=False)
    amount = models.IntegerField(blank=True, null=True)

    @property
    def tdate(self):
        return self.fdate + timedelta(days=(self.days-1))


class ProlongationAqua(GenericProlongation, models.Model):

    """
    Prolongation for the Client Club Card.
    """
    date = models.DateTimeField()
    client_aqua = models.ForeignKey(ClientAquaAerobics)
    days = models.SmallIntegerField()
    amount = models.DecimalField(max_digits=15, decimal_places=2,)
    is_paid = models.BooleanField(default=False)

    @property
    def parent(self):
        return self.client_aqua

    def save(self, *args, **kwargs):
        if not self.pk:
            self.parent_upd(self,)
        super(ProlongationAqua, self).save(*args, **kwargs)


class AquaAerobicsClients(models.Model):

    """
    External clients for the ClientAquaAerobics.
    """
    date = models.DateTimeField(auto_now_add=True)
    client = models.ForeignKey(Client, )
    client_aqua = models.ForeignKey(ClientAquaAerobics,)

    class Meta:
        unique_together = ('client', 'client_aqua')


class ClientAquaAerobicsFull(models.Model):

    """
    The clients Aqua Aerobics card FULL JOIN
    with Aqua Aerobics Clients (External clients for the ClientAquaAerobics),
    history and status.

    Date start - the date for the start period of activation.
    Date begin - is start of using the card.

    """
    date = models.DateTimeField(auto_now_add=True)
    date_start = models.DateField()
    date_begin = models.DateField()
    date_end = models.DateField()
    client = models.ForeignKey(Client, )
    aqua_aerobics = models.ForeignKey(AquaAerobics, )
    status = models.SmallIntegerField(default=2, blank=True, )
    """
    status valid data:
    0 - disabled
    1 - active
    2 - prospect
    """

    class Meta:
        db_table = 'v_external_aqua'
        managed = False

    @property
    def name(self):
        return self.aqua_aerobics.name

    @property
    def rest_days(self):
        if not self.date_end:
            return None
        rest_days = (self.date_end - date.today()).days
        if rest_days < 1:
            return 0
        return rest_days

    @property
    def rest_visits(self):
        if self.aqua_aerobics.max_visit == 99999:
            return '-'
        used = UseClientAquaAerobics.objects.filter(client_aqua_aerobics=self)\
                                            .count()
        return self.aqua_aerobics.max_visit - used

    @property
    def is_online(self):
        return UseClientAquaAerobics.objects.filter(client_aqua_aerobics=self,
                                                    end__isnull=True).count()

    @property
    def is_frozen(self):
        freezes = FreezeAqua.objects\
                            .filter(client_aqua=self,
                                    fdate__lte=date.today())
        for f in freezes:
            if f.tdate >= date.today():
                return True
        return False


class ClientTicket(GenericProperty, models.Model):

    """
    The clients tickets,
    history and status.

    Date start - the date for the start period of activation.
    Date begin - is start of using the card.
    """

    freeze_class = 'FreezeTicket'

    date = models.DateTimeField(auto_now_add=True)
    date_start = models.DateField(blank=True)
    date_begin = models.DateField(null=True, blank=True)
    date_end = models.DateField(null=True, blank=True)
    client = models.ForeignKey(Client, )
    ticket = models.ForeignKey(Ticket, )
    discount_type = models.ForeignKey(Discount, blank=True, null=True)
    discount_amount = models.FloatField(blank=True, null=True)
    bonus_type = models.ForeignKey(Discount, blank=True, null=True,
                                   related_name="ticket_bonus_type")
    bonus_amount = models.FloatField(blank=True, null=True)
    status = models.SmallIntegerField(default=2, blank=True, )
    printed = models.BooleanField(default=False)
    block_comment = models.CharField(max_length=150, blank=True, null=True)
    """
    status valid data:
    0 - disabled
    1 - active
    2 - prospect
    """

    @property
    def client_name(self):
        return self.client.full_name

    @property
    def name(self):
        return self.ticket.name

    @property
    def is_frozen(self):
        freezes = FreezeTicket.objects\
            .filter(client_ticket=self,
                    fdate__lte=date.today())
        for f in freezes:
            if f.tdate >= date.today():
                return True
        return False

    @property
    def rest_days(self):
        rest_days = (self.date_end - date.today()).days
        if rest_days < 1:
            return 0
        return rest_days

    @property
    def rest_visits(self):
        if self.ticket.max_visit == 99999:
            return '-'
        used = UseClientTicket.objects.filter(client_ticket=self).count()
        return self.ticket.max_visit - used

    @property
    def is_online(self):
        return UseClientTicket.objects.filter(client_ticket=self,
                                              end__isnull=True).count()


class FreezeTicket(models.Model):

    """Freeze ticket."""
    product = 'client_ticket'

    date = models.DateTimeField(auto_now_add=True)
    client_ticket = models.ForeignKey(ClientTicket)
    fdate = models.DateField()
    days = models.SmallIntegerField()
    is_paid = models.BooleanField(default=False)
    amount = models.IntegerField(blank=True, null=True)

    @property
    def tdate(self):
        return self.fdate + timedelta(days=(self.days-1))


class ProlongationTicket(GenericProlongation, models.Model):

    """
    Prolongation for the Client Ticket.
    """
    date = models.DateTimeField()
    client_ticket = models.ForeignKey(ClientTicket)
    days = models.SmallIntegerField()
    amount = models.DecimalField(max_digits=15, decimal_places=2,)
    is_paid = models.BooleanField(default=False)

    @property
    def parent(self):
        return self.client_ticket

    def save(self, *args, **kwargs):
        if not self.pk:
            self.parent_upd(self,)
        super(ProlongationTicket, self).save(*args, **kwargs)


class ClientPersonal(models.Model):

    """
    The clients personals,
    history and status.

    Date start - the date for the start period of activation.
    Date begin - is start of using the card.

    """
    date = models.DateTimeField(auto_now_add=True)
    date_start = models.DateField(blank=True)
    date_begin = models.DateField(blank=True)
    date_end = models.DateField(blank=True)
    client = models.ForeignKey(Client, )
    personal = models.ForeignKey(Personal, )
    status = models.SmallIntegerField(default=2, blank=True, )
    """
    status valid data:
    0 - disabled
    1 - active
    2 - prospect
    """

    @property
    def client_name(self):
        return self.client.full_name

    @property
    def name(self):
        return self.personal.name

    @property
    def rest_days(self):
        rest_days = (self.date_end - date.today()).days
        if rest_days < 1:
            return 0
        return rest_days

    @property
    def rest_visits(self):
        if self.personal.max_visit == 99999:
            return '-'
        used = UseClientPersonal.objects.filter(client_personal=self).count()
        return self.personal.max_visit - used

    @property
    def is_online(self):
        return UseClientPersonal.objects.filter(client_personal=self,
                                                end__isnull=True).count()


class ClientTiming(models.Model):

    """
    The clients timings,
    history and status.

    Date start - the date for the start period of activation.
    Date begin - is start of using the card.

    """
    date = models.DateTimeField(auto_now_add=True)
    date_start = models.DateField(blank=True)
    date_begin = models.DateField(blank=True)
    date_end = models.DateField(blank=True)
    client = models.ForeignKey(Client, )
    timing = models.ForeignKey(Timing, )
    status = models.SmallIntegerField(default=2, blank=True, )
    """
    status valid data:
    0 - disabled
    1 - active
    2 - prospect
    """

    @property
    def client_name(self):
        return self.client.full_name

    @property
    def name(self):
        return self.timing.name

    @property
    def rest_days(self):
        rest_days = (self.date_end - date.today()).days
        if rest_days < 1:
            return 0
        return rest_days

    @property
    def rest_minutes(self):
        used = UseClientTiming.objects.filter(client_timing=self)\
                                      .aggregate(sum=Sum('minutes'))
        if used['sum']:
            return self.timing.minutes - used['sum']
        return self.timing.minutes


class UseClientClubCard(models.Model):

    """
    Log information about use the Client Club Card.
    """
    date = models.DateTimeField(auto_now_add=True)
    end = models.DateTimeField(blank=True, null=True)
    client_club_card = models.ForeignKey(ClientClubCard)

    def save(self, *args, **kwargs):
        if not self.pk:
            is_first = UseClientClubCard.objects\
                .filter(client_club_card=self.client_club_card)\
                .count()
            if is_first == 0:
                cc = self.client_club_card
                cc.date_begin = date.today()
                cc.date_end = date_end(date.today(), cc.club_card)
                cc.save()
            if self.client_club_card.is_frozen:
                self.client_club_card.escape_frozen()
        if self.end and self.client_club_card.rest_visits < 1:
            # set status not activate
            self.client_club_card.deactivate()
        super(UseClientClubCard, self).save(*args, **kwargs)


class ClubCardTrains(models.Model):

    """
    The list of trainings of the visit by club card.
    """
    visit = models.ForeignKey(UseClientClubCard)
    training = models.ForeignKey(Training)

    def name(self):
        return self.training.name


class UseClientAquaAerobics(models.Model):

    """
    Log information about use the Client AquaAerobics.
    """
    date = models.DateTimeField(auto_now_add=True)
    end = models.DateTimeField(blank=True, null=True)
    client_aqua_aerobics = models.ForeignKey(ClientAquaAerobics)

    def save(self, *args, **kwargs):
        if not self.pk:
            is_first = UseClientAquaAerobics.objects.filter(
                client_aqua_aerobics=self.client_aqua_aerobics).count()
            if is_first == 0:
                aqua = self.client_aqua_aerobics
                aqua.date_begin = date.today()
                aqua.date_end = date_end(date.today(), aqua.aqua_aerobics)
                aqua.save()
            if self.client_aqua_aerobics.is_frozen:
                self.client_aqua_aerobics.escape_frozen()
        super(UseClientAquaAerobics, self).save(*args, **kwargs)


class UseClientTicket(models.Model):

    """
    Log information about use the Client Ticket.
    """
    date = models.DateTimeField(auto_now_add=True)
    end = models.DateTimeField(blank=True, null=True)
    client_ticket = models.ForeignKey(ClientTicket)

    def save(self, *args, **kwargs):
        if not self.pk:
            is_first = UseClientTicket.objects.filter(
                client_ticket=self.client_ticket).count()
            if is_first == 0:
                ticket = self.client_ticket
                ticket.date_begin = date.today()
                ticket.date_end = date_end(date.today(), ticket.ticket)
                ticket.save()
            if self.client_ticket.is_frozen:
                self.client_ticket.escape_frozen()
        super(UseClientTicket, self).save(*args, **kwargs)


class UseClientPersonal(models.Model):

    """
    Log information about use the Client Personal.
    """
    date = models.DateTimeField(auto_now_add=True)
    end = models.DateTimeField(blank=True, null=True)
    client_personal = models.ForeignKey(ClientPersonal)


class UseClientTiming(models.Model):

    """
    Log information about use the Client Timing.
    """
    date = models.DateTimeField(auto_now_add=True)
    end = models.DateTimeField(blank=True, null=True)
    client_timing = models.ForeignKey(ClientTiming)
    minutes = models.IntegerField(default=1, blank=True)


class ExtClientClubCard(models.Model):

    """
    Extended clients for the Client Club Card
    where clients_count > 1.
    """
    client_club_card = models.ForeignKey(ClientClubCard)
    client = models.ForeignKey(Client, )


class ClientOnline(models.Model):

    """
    Clients who has not end date in the use tables.
    """
    client = models.ForeignKey(Client, )
    date = models.DateTimeField(auto_now_add=True)
    product = models.CharField(max_length=50)

    class Meta:
        db_table = 'v_client_online'
        managed = False


def date_end(date_begin, obj):
    """
    Return date end for the obj
    """
    # the first day used
    date_from = date_begin - timedelta(days=1)
    if obj.period.is_month:
        months = obj.period.value
        return date_from + relativedelta(months=months)
    else:
        days = obj.period.value
        return date_from + timedelta(days=days)
