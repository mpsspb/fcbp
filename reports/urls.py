# -*- coding: utf-8 -*-
from rest_framework import routers

from .views import (
	Sales, Visits, Birthdays, ActiveClubCard, CreditsClubCard, NewUid,
	CommonList, FullList, RepFitnessClubCard)


router = routers.SimpleRouter()
router.register(r'sales', Sales,  base_name='sales')
router.register(r'visits', Visits,  base_name='visits')
router.register(r'birthdays', Birthdays,  base_name='birthdays')
router.register(r'acc', ActiveClubCard,  base_name='acc')
router.register(r'ccc', CreditsClubCard,  base_name='ccc')
router.register(r'new_uid', NewUid,  base_name='new_uid')
router.register(r'cl', CommonList,  base_name='cl')
router.register(r'fl', FullList,  base_name='fl')
router.register(r'fcc', RepFitnessClubCard,  base_name='fcc')

urlpatterns = router.urls
