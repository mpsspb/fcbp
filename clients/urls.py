from django.conf.urls import patterns, include, url

from rest_framework import routers

from .views import *
from .advanced_search import ClientSearchViewSet


router = routers.SimpleRouter()
router.register(r'client', ClientViewSet, 'Client')

router.register(r'clubcard', ClientClubCardViewSet, 'ClubCard')
router.register(r'freezecc', FreezeClubCardViewSet, 'FreezeClubCard')
router.register(r'ownercc', OwnersClubCardViewSet, 'OwnersClubCard')

router.register(r'aquaaerobics', ClientAquaAerobicsViewSet,
                'AquaAerobics')
router.register(r'ticket', ClientTicketViewSet, 'Ticket')
router.register(r'personal', ClientPersonalViewSet, 'ClientPersonal')
router.register(r'timing', ClientTimingViewSet, 'ClientTiming')

router.register(r'useclubcard', UseClientClubCardViewSet, 'UseClubCard')
router.register(r'useaquaaerobics', UseClientAquaAerobicsViewSet,
                'UseAquaAerobics')
router.register(r'useticket', UseClientTicketViewSet, 'UseTicket')
router.register(r'usepersonal', UseClientPersonalViewSet, 'UseClientPersonal')
router.register(r'usetiming', UseClientTimingViewSet, 'UseClientTiming')
router.register(r'personalclubcard', PersonalClubCardViewSet, 'PClubCard')
router.register(r'fitness', FitnessClubCardViewSet, 'FitnessClubCard')
router.register(r'prolongation', ProlongationClubCardViewSet, 'prolongation')
router.register(
    r'aquaprolongation', ProlongationAquaViewSet, 'aquaprolongation')
router.register(
    r'prolongationticket', ProlongationTicketViewSet, 'prolongationticket')
router.register(
    r'prolongationticket_personal',
    ProlongationPersonalViewSet,
    'prolongationticket_personal')

router.register(r'advanced_search', ClientSearchViewSet, 'advanced_search')


urlpatterns = router.urls

urlpatterns += url(r'^archive/', include('clients.urls_archive')),
