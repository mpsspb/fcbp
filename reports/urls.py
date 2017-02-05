# -*- coding: utf-8 -*-
from rest_framework import routers

from .views import (
	Sales, Visits, Birthdays, ActiveClubCard, CreditsClubCard, NewUid)


router = routers.SimpleRouter()
router.register(r'sales', Sales,  base_name='sales')
router.register(r'visits', Visits,  base_name='visits')
router.register(r'birthdays', Birthdays,  base_name='birthdays')
router.register(r'acc', ActiveClubCard,  base_name='acc')
router.register(r'ccc', CreditsClubCard,  base_name='ccc')
router.register(r'new_uid', NewUid,  base_name='new_uid')

urlpatterns = router.urls
