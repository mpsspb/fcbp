# -*- coding: utf-8 -*-
from rest_framework import routers

from .views import Sales


router = routers.SimpleRouter()
router.register(r'sales', Sales,  base_name='sales')

urlpatterns = router.urls
