from datetime import date, timedelta
from django.db import models
from django.db.models import Sum

from products.models import ClubCard, AquaAerobics, Ticket, Personal, Timing
from employees.models import Employee


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
    passport = models.TextField(null=True, blank=True)
    phone = models.IntegerField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    avatar = models.ImageField(upload_to="avatar/", null=True, blank=True)

    introductory_date = models.DateTimeField(blank=True, null=True)
    introductory_employee = models.ForeignKey(Employee, blank=True, null=True)

    @property
    def full_name(self,):
        return "%s %s %s" % (self.last_name, self.first_name, self.patronymic)

    @property
    def online_clubcard(self,):
        return ClientOnline.objects.filter(client=self, product='clubcard')\
                           .exists()

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


class ClientClubCard(models.Model):
    """
    The clients club card,
    history and status.

    Date start - the date for the start period of activation.
    Date begin - is start of using the card.

    """
    date = models.DateTimeField(auto_now_add=True)
    date_start = models.DateField(blank=True)
    date_begin = models.DateField(blank=True)
    date_end = models.DateField(blank=True)
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
    def client_name(self):
        return self.client.full_name

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
        used = UseClientClubCard.objects.filter(client_club_card=self).count()
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

    def escape_frozen(self):
        freezes = FreezeClubCard.objects\
                                .filter(client_club_card=self,
                                        fdate__lte=date.today())
        for f in freezes:
            if f.tdate >= date.today():
                days_freeze = (date.today() - f.fdate).days
                if not f.is_paid:
                    days_back = (f.tdate - date.today()).days + 1
                    self.date_end = self.date_end - timedelta(days_back)
                    self.save()
                f.days = days_freeze
                f.save()


class ProlongationClubCard(models.Model):
    """
    Guest training for the Client Club Card.
    """
    date = models.DateTimeField(auto_now_add=True)
    client_club_card = models.ForeignKey(ClientClubCard)
    days = models.SmallIntegerField()
    amount = models.DecimalField(max_digits=15, decimal_places=2,)
    is_paid = models.BooleanField(default=False)


class GuestClubCard(models.Model):
    """
    Guest training for the Client Club Card.
    """
    date = models.DateTimeField(auto_now_add=True)
    client_club_card = models.ForeignKey(ClientClubCard)
    guest = models.CharField(max_length=60)
    born = models.DateField()
    phone = models.BigIntegerField(null=True, blank=True)


class FitnessClubCard(models.Model):
    """
    Fitness  testing discount for the Client Club Card.
    """
    date = models.DateTimeField(auto_now_add=True)
    client_club_card = models.ForeignKey(ClientClubCard)
    personal = models.ForeignKey(Employee, )

    @property
    def employee(self):
        return self.personal.initials


class PersonalClubCard(models.Model):
    """
    Personal training discount for the Client Club Card.
    """
    date = models.DateTimeField(auto_now_add=True)
    client_club_card = models.ForeignKey(ClientClubCard)
    personal = models.ForeignKey(Employee)

    @property
    def employee(self):
        return self.personal.initials


class FreezeClubCard(models.Model):
    """
    Freeze club card.
    """
    date = models.DateTimeField(auto_now_add=True)
    client_club_card = models.ForeignKey(ClientClubCard)
    fdate = models.DateField()
    days = models.SmallIntegerField()
    is_paid = models.BooleanField(default=False)

    @property
    def tdate(self):
        return self.fdate + timedelta(days=(self.days-1))


class ClientAquaAerobics(models.Model):
    """
    The clients Aqua Aerobics card,
    history and status.

    Date start - the date for the start period of activation.
    Date begin - is start of using the card.

    """
    date = models.DateTimeField(auto_now_add=True)
    date_start = models.DateField(blank=True)
    date_begin = models.DateField(blank=True)
    date_end = models.DateField(blank=True)
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
    def client_name(self):
        return self.client.full_name

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
        used = UseClientAquaAerobics.objects.filter(client_aqua_aerobics=self)\
                                            .count()
        return self.aqua_aerobics.max_visit - used

    @property
    def is_online(self):
        return UseClientAquaAerobics.objects.filter(client_aqua_aerobics=self,
                                                    end__isnull=True).count()


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


class ClientTicket(models.Model):
    """
    The clients tickets,
    history and status.

    Date start - the date for the start period of activation.
    Date begin - is start of using the card.

    """
    date = models.DateTimeField(auto_now_add=True)
    date_start = models.DateField(blank=True)
    date_begin = models.DateField(blank=True)
    date_end = models.DateField(blank=True)
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
    def client_name(self):
        return self.client.full_name

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
        used = UseClientTicket.objects.filter(client_ticket=self).count()
        return self.ticket.max_visit - used

    @property
    def is_online(self):
        return UseClientTicket.objects.filter(client_ticket=self,
                                              end__isnull=True).count()


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
