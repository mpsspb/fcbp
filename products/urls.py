from django.conf.urls import patterns, include, url

from rest_framework import routers

from .views import PeriodViewSet, ClubCardViewSet, AquaAerobicsViewSet


router = routers.SimpleRouter()
router.register(r'periods', PeriodViewSet)
router.register(r'club_cards', ClubCardViewSet)
router.register(r'aquaaerobics', AquaAerobicsViewSet)

urlpatterns = router.urls