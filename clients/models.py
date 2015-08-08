from django.db import models

class Client(models.Model):
    """
    Clients data.
    """
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    patronymic = models.CharField(max_length=30)
    born = models.DateField()

    gender = models.SmallIntegerField(default=0, blank=True)
    mobile = models.BigIntegerField(null=True, blank=True)
    address = models.CharField(max_length=100, null=True, blank=True)
    passport = models.TextField(null=True, blank=True)
    phone = models.IntegerField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    avatar = models.ImageField(upload_to="avatar/", blank=True)
