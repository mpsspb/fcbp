from django.db import models


class Position(models.Model):
    """
    Positions of the employees.
    """
    name = models.CharField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True, blank=True)
