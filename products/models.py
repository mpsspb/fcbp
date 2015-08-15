from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Discount(models.Model):
    """
    Available discounts.
    """
    value = models.SmallIntegerField(
            validators = [MinValueValidator(0), MaxValueValidator(100)])
    is_active = models.BooleanField(default=True)


class Period(models.Model):
    """
    Period for club card types.
    Default values in month, other way in days.
    """
    value = models.SmallIntegerField(unique=True)
    is_month = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)


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
