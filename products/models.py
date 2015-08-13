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
    is_active = models.BooleanField(default=True)
    period_freeze = models.IntegerField(default=0)
    freeze_times = models.IntegerField(default=0)
    period_activation = models.IntegerField(default=0)
    guest_training = models.SmallIntegerField(default=0)
    fitness_testing_discount = models.BooleanField(default=False)
    personal_training = models.BooleanField(default=False)
    price = models.DecimalField(max_digits=15, decimal_places=2,)

    @property
    def period_data(self):
        return self.period
    
