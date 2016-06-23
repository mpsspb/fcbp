from django.conf.urls import patterns, include, url

from rest_framework import routers

from .views_archive import (
    ClientClubCardViewSet, ClientAquaAerobicsViewSet, ClientTicketViewSet)


router = routers.SimpleRouter()

router.register(r'clubcard', ClientClubCardViewSet, 'ClubCard')
router.register(r'aquaaerobics', ClientAquaAerobicsViewSet, 'Aqua')
router.register(r'ticket', ClientTicketViewSet, 'Ticket')

urlpatterns = router.urls
