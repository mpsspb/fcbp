from django.conf.urls import patterns, include, url

from rest_framework import routers

from .views import PeriodViewSet


router = routers.SimpleRouter()
router.register(r'periods', PeriodViewSet)

urlpatterns = router.urls