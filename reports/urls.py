# -*- coding: utf-8 -*-
from rest_framework import routers

from .views import Sales, Visits, Birthdays


router = routers.SimpleRouter()
router.register(r'sales', Sales,  base_name='sales')
router.register(r'visits', Visits,  base_name='visits')
router.register(r'birthdays', Birthdays,  base_name='birthdays')

urlpatterns = router.urls
