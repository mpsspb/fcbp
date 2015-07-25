from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    is_admin = models.BooleanField(default=False)
    is_manager = models.BooleanField(default=False)
    is_reception = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'

    def __unicode__(self):
        return self.username
