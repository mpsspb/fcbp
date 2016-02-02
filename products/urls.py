from django.conf.urls import patterns, include, url

from rest_framework import routers

from .views import (
                PeriodViewSet, ClubCardViewSet, AquaAerobicsViewSet,
                SportViewSet, TicketViewSet, PersonalViewSet,
                PersonalPositionViewSet, TimingViewSet, DiscountViewSet,
                TrainingViewSet)


router = routers.SimpleRouter()
router.register(r'periods', PeriodViewSet)
router.register(r'club_cards', ClubCardViewSet)
router.register(r'aquaaerobics', AquaAerobicsViewSet)
router.register(r'sports', SportViewSet)
router.register(r'training', TrainingViewSet)
router.register(r'tickets', TicketViewSet)
router.register(r'personal', PersonalViewSet)
router.register(r'personalpos', PersonalPositionViewSet)
router.register(r'timing', TimingViewSet)
router.register(r'discount', DiscountViewSet)

urlpatterns = router.urls
