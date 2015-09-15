import json

from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.decorators import list_route
from rest_framework.pagination import PageNumberPagination

from .models import *
from .serializers import *
from .use_serializers import *


class ClientResultsSetPagination(PageNumberPagination):
    page_size = 10000
    page_size_query_param = 'page_size'
    max_page_size = 10000


class ClientViewSet(viewsets.ModelViewSet):

    serializer_class = ClientSerializer
    pagination_class = ClientResultsSetPagination

    def get_queryset(self):
        """
        Optionally restricts the returned clients,
        by filtering against a `letter` query parameter in the URL.
        """
        queryset = Client.objects\
                     .order_by('last_name', 'first_name', 'patronymic')

        letter = self.request.query_params.get('letter', None)
        if letter is not None:
            queryset = queryset.filter(last_name__istartswith=letter)

        return queryset


class ClientClubCardViewSet(viewsets.ModelViewSet):
    queryset = ClientClubCard.objects.order_by('-date')
    serializer_class = ClientClubCardSerializer


class ClientAquaAerobicsViewSet(viewsets.ModelViewSet):
    queryset = ClientAquaAerobics.objects.order_by('-date')
    serializer_class = ClientAquaAerobicsSerializer


class ClientTicketViewSet(viewsets.ModelViewSet):
    queryset = ClientTicket.objects.order_by('-date')
    serializer_class = ClientTicketSerializer


class ClientPersonalViewSet(viewsets.ModelViewSet):
    queryset = ClientPersonal.objects.order_by('-date')
    serializer_class = ClientPersonalSerializer


class ClientTimingViewSet(viewsets.ModelViewSet):
    queryset = ClientTiming.objects.order_by('-date')
    serializer_class = ClientTimingSerializer


class UseClientClubCardViewSet(viewsets.ModelViewSet):
    queryset = UseClientClubCard.objects.order_by('-date')
    serializer_class = UseClientClubCardSerializer


class UseClientAquaAerobicsViewSet(viewsets.ModelViewSet):
    queryset = UseClientAquaAerobics.objects.order_by('-date')
    serializer_class = UseClientAquaAerobicsSerializer


class UseClientTicketViewSet(viewsets.ModelViewSet):
    queryset = UseClientTicket.objects.order_by('-date')
    serializer_class = UseClientTicketSerializer


class UseClientPersonalViewSet(viewsets.ModelViewSet):
    queryset = UseClientPersonal.objects.order_by('-date')
    serializer_class = UseClientPersonalSerializer


class UseClientTimingViewSet(viewsets.ModelViewSet):
    queryset = UseClientTiming.objects.order_by('-date')
    serializer_class = UseClientTimingSerializer
