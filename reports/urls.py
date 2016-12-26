# -*- coding: utf-8 -*-
from rest_framework import routers

from .views import Sales, Visits


router = routers.SimpleRouter()
router.register(r'sales', Sales,  base_name='sales')
router.register(r'visits', Visits,  base_name='visits')

urlpatterns = router.urls
