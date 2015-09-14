from datetime import date, timedelta
from django.db import models

from products.models import ClubCard, AquaAerobics, Ticket, Personal, Timing


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

    mobile = models.BigIntegerField(null=True, blank=True)
    gender = models.SmallIntegerField(default=0, blank=True)
    address = models.CharField(max_length=100, null=True, blank=True)
    passport = models.TextField(null=True, blank=True)
    phone = models.IntegerField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    avatar = models.ImageField(upload_to="avatar/", null=True, blank=True)

    @property
    def full_name(self,):
        return "%s %s %s" % (self.last_name, self.first_name, self.patronymic)

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
        super(Client, self).save(*args, **kwargs)


class ClientClubCard(models.Model):
    """
    The clients club card, 
    history and status.

    Date start - the date for the start period of activation.
    Date begin - is start of using the card.

    """
    date = models.DateTimeField(auto_now_add=True)
    date_start = models.DateField()
    date_begin = models.DateField()
    date_end = models.DateField()
    client = models.ForeignKey(Client, )
    club_card = models.ForeignKey(ClubCard, )
    status = models.SmallIntegerField(default=2, blank=True, )
    """
    status valid data:
    0 - disabled
    1 - active
    2 - prospect
    """

    @property
    def name(self):
        return self.club_card.name

    @property
    def rest_days(self):
        rest_days = (self.date_end - date.today()).days
        if rest_days < 1:
            return 0
        return rest_days

    @property
    def rest_visits(self):
        if self.club_card.max_visit == 99999:
            return '-'
        return self.club_card.max_visit
        

class ClientAquaAerobics(models.Model):
    """
    The clients Aqua Aerobics card, 
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

    @property
    def name(self):
        return self.aqua_aerobics.name

    @property
    def rest_days(self):
        rest_days = (self.date_end - date.today()).days
        if rest_days < 1:
            return 0
        return rest_days

    @property
    def rest_visits(self):
        if self.aqua_aerobics.max_visit == 99999:
            return '-'
        return self.aqua_aerobics.max_visit


class ClientTicket(models.Model):
    """
    The clients tickets, 
    history and status.

    Date start - the date for the start period of activation.
    Date begin - is start of using the card.

    """
    date = models.DateTimeField(auto_now_add=True)
    date_start = models.DateField()
    date_begin = models.DateField()
    date_end = models.DateField()
    client = models.ForeignKey(Client, )
    ticket = models.ForeignKey(Ticket, )
    status = models.SmallIntegerField(default=2, blank=True, )
    """
    status valid data:
    0 - disabled
    1 - active
    2 - prospect
    """

    @property
    def name(self):
        return self.ticket.name

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
        return self.ticket.max_visit


class ClientPersonal(models.Model):
    """
    The clients personals, 
    history and status.

    Date start - the date for the start period of activation.
    Date begin - is start of using the card.

    """
    date = models.DateTimeField(auto_now_add=True)
    date_start = models.DateField()
    date_begin = models.DateField()
    date_end = models.DateField()
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
        return self.personal.max_visit


class ClientTiming(models.Model):
    """
    The clients timings, 
    history and status.

    Date start - the date for the start period of activation.
    Date begin - is start of using the card.

    """
    date = models.DateTimeField(auto_now_add=True)
    date_start = models.DateField()
    date_begin = models.DateField()
    date_end = models.DateField()
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
        return self.timing.minutes


class UseClientClubCard(models.Model):
    """
    Log information about use the Client Club Card.
    """
    date = models.DateTimeField(auto_now_add=True)
    end = models.DateField(blank=True, null=True)
    client_club_card = models.ForeignKey(ClientClubCard)


class UseClientAquaAerobics(models.Model):
    """
    Log information about use the Client AquaAerobics.
    """
    date = models.DateTimeField(auto_now_add=True)
    end = models.DateField(blank=True, null=True)
    client_aqua_aerobics = models.ForeignKey(ClientAquaAerobics)


class UseClientTicket(models.Model):
    """
    Log information about use the Client Ticket.
    """
    date = models.DateTimeField(auto_now_add=True)
    end = models.DateField(blank=True, null=True)
    client_ticket = models.ForeignKey(ClientTicket)


class UseClientPersonal(models.Model):
    """
    Log information about use the Client Personal.
    """
    date = models.DateTimeField(auto_now_add=True)
    end = models.DateField(blank=True, null=True)
    client_personal = models.ForeignKey(ClientPersonal)


class UseClientTiming(models.Model):
    """
    Log information about use the Client Timing.
    """
    date = models.DateTimeField(auto_now_add=True)
    end = models.DateField(blank=True, null=True)
    client_timing = models.ForeignKey(ClientTiming)
    minutes = models.IntegerField(default=1, blank=True)
