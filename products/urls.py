from django.conf.urls import patterns, include, url

from rest_framework import routers

from .views import PeriodViewSet, ClubCardViewSet


router = routers.SimpleRouter()
router.register(r'periods', PeriodViewSet)
router.register(r'club_cards', ClubCardViewSet)

urlpatterns = router.urls