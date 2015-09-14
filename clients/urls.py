from django.conf.urls import patterns, include, url

from rest_framework import routers

from .views import ClientViewSet, UseClientClubCardViewSet
from .views import UseClientAquaAerobicsViewSet, UseClientTicketViewSet
from .views import UseClientPersonalViewSet, UseClientTimingViewSet

router = routers.SimpleRouter()
router.register(r'client', ClientViewSet, 'Client')

router.register(r'useclubcard', UseClientClubCardViewSet, 'UseClubCard')
router.register(r'useaquaaerobics', UseClientAquaAerobicsViewSet,
                'UseAquaAerobics')
router.register(r'useticket', UseClientTicketViewSet, 'UseTicket')
router.register(r'usepersonal', UseClientPersonalViewSet, 'UseClientPersonal')
router.register(r'usetiming', UseClientTimingViewSet, 'UseClientTiming')

urlpatterns = router.urls
