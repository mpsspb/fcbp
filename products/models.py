from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.core import serializers

from employees.models import Position


class Discount(models.Model):
    """
    Available discounts.
    """
    is_active = models.BooleanField(default=True)
    description = models.CharField(max_length=150, unique=True)


class Period(models.Model):
    """
    Period for club card types.
    Default values in month, other way in days.
    """
    value = models.SmallIntegerField()
    is_month = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        unique_together = ('value', 'is_month')


class ClubCard(models.Model):
    """
    Club card types.
    """
    name = models.CharField(max_length=255, unique=True)
    max_visit = models.IntegerField()
    period = models.ForeignKey(Period, )
    is_full_time = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True, blank=True)
    period_freeze = models.IntegerField(default=0, blank=True)
    freeze_times = models.IntegerField(default=0, blank=True)
    period_prolongation = models.IntegerField(default=0, blank=True)
    clients_count = models.IntegerField(default=1, blank=True)
    period_activation = models.IntegerField(default=0, blank=True)
    guest_training = models.SmallIntegerField(default=0, blank=True)
    fitness_testing_discount = models.BooleanField(default=False, blank=True)
    personal_training = models.BooleanField(default=False, blank=True)
    price = models.DecimalField(max_digits=15, decimal_places=2,)

    @property
    def period_data(self):
        return self.period


class AquaAerobics(models.Model):
    """
    Aqua Aerobics types.
    """
    name = models.CharField(max_length=255, unique=True)
    max_visit = models.IntegerField()
    period = models.ForeignKey(Period, )
    is_full_time = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True, blank=True)
    clients_count = models.IntegerField(default=1, blank=True)
    period_prolongation = models.IntegerField(default=0, blank=True)
    price = models.DecimalField(max_digits=15, decimal_places=2,)

    @property
    def period_data(self):
        return self.period


class Sport(models.Model):
    """
    Sports types.
    """
    name = models.CharField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True, blank=True)


class Training(models.Model):
    """
    Training types.
    """
    name = models.CharField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True, blank=True)


class Ticket(models.Model):
    """
    Ticket types
    """
    name = models.CharField(max_length=255, unique=True)
    period = models.ForeignKey(Period, )
    sport = models.ForeignKey(Sport, )
    is_full_time = models.BooleanField(default=True, blank=True)
    max_visit = models.IntegerField()
    period_prolongation = models.IntegerField(default=0, blank=True)
    is_active = models.BooleanField(default=True, blank=True)
    price = models.DecimalField(max_digits=15, decimal_places=2,)

    @property
    def period_data(self):
        return self.period

    @property
    def sport_data(self):
        return self.sport

    @property
    def sport_name(self):
        return self.sport.name


class Personal(models.Model):
    """
    Personal training.
    """
    name = models.CharField(max_length=255, unique=True)
    period = models.ForeignKey(Period, )
    max_visit = models.IntegerField()
    clients_count = models.IntegerField(default=1, blank=True)
    is_full_time = models.BooleanField(default=True, blank=True)
    is_active = models.BooleanField(default=True, blank=True)
    price = models.DecimalField(max_digits=15, decimal_places=2,)
    period_prolongation = models.IntegerField(default=0, blank=True)

    @property
    def period_data(self):
        return self.period


class PersonalPosition(models.Model):
    """
    Trainer position for personal.
    """
    personal = models.ForeignKey(Personal, blank=True, null=True)
    position = models.ForeignKey(Position, blank=True)

    class Meta:
        unique_together = ('personal', 'position')


class Timing(models.Model):
    """
    Products with counting time.
    The time in minutes.
    """
    name = models.CharField(max_length=255, unique=True)
    period = models.ForeignKey(Period, )
    price = models.DecimalField(max_digits=15, decimal_places=2,)
    period_prolongation = models.IntegerField(default=0, blank=True)
    period_freeze = models.IntegerField(default=0, blank=True)
    clients_count = models.IntegerField(default=1, blank=True)
    minutes = models.IntegerField(default=1, blank=True)
    is_active = models.BooleanField(default=True, blank=True)

    @property
    def period_data(self):
        return self.period
