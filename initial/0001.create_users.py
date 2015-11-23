#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
import inspect
import django


if __name__ == "__main__":

    # add project dir to sys path
    fname = inspect.currentframe()
    folder = os.path.split(os.path.split(inspect.getfile(fname))[0])[0]
    if folder not in sys.path:
        sys.path.insert(0, folder)
    os.environ.setdefault("DJANGO_SETTINGS_MODULE",  "fcbp.settings")
    django.setup()
    from users.models import User
    u = User.objects.get_or_create(username='admin')[0]
    u.is_admin = True
    u.set_password('1')
    u.save()
