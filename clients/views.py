import json
from datetime import datetime

from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.decorators import list_route, detail_route
from rest_framework.pagination import PageNumberPagination

from .models import *
from .forms import *
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

    @list_route(methods=['get'], )
    def online(self, request):
        """
        List clients inside the club.
        """
        clients = ClientOnline.objects.all().values('client_id')
        queryset = Client.objects.filter(pk__in=clients)
        serializer = ClientSerializer(queryset, many=True)
        return Response(serializer.data)

    @list_route(methods=['post'], )
    def search(self, request):
        """
        Search clients by carb or uid or istartswith last_name.
        """
        search = request.data['search']
        try:
            search = int(search)
            queryset = Client.objects.filter(card=search)
            queryset = queryset | Client.objects.filter(uid=search)
        except:
            queryset = Client.objects.filter(last_name__istartswith=search)
        serializer = ClientSerializer(queryset, many=True)
        return Response(serializer.data)

    @list_route(methods=['post'], )
    def full_search(self, request):
        """
        Search clients by carb or uid or istartswith last_name.
        """
        queryset = Client.objects.filter(pk=-1)
        last_name = request.data.get('last_name', None)
        if last_name:
            queryset = queryset |\
                       Client.objects\
                             .filter(last_name__istartswith=last_name)
        first_name = request.data.get('first_name', None)
        if first_name:
            queryset = queryset |\
                       Client.objects\
                             .filter(first_name__istartswith=first_name)
        patronymic = request.data.get('patronymic', None)
        if patronymic:
            queryset = queryset |\
                       Client.objects\
                             .filter(patronymic__istartswith=patronymic)

        serializer = ClientSerializer(queryset, many=True)
        return Response(serializer.data)

    @detail_route(methods=['post'], )
    def introductory(self, request, pk):
        """
        Set introductory for the user.
        """
        client = self.get_object()
        form = FormClientIntro(request.data, instance=client)
        if form.is_valid():
            form.save()
        else:
            print form.errors
        return Response({'status': 'ok'}, status=status.HTTP_202_ACCEPTED)


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

    @list_route(methods=['post'], )
    def exit(self, request):
        card_id = request.data['client_club_card']
        exit = UseClientClubCard.objects\
                                .filter(client_club_card=card_id)\
                                .update(end=datetime.now())
        return Response({'status': 'ok'}, status=status.HTTP_202_ACCEPTED)


class UseClientAquaAerobicsViewSet(viewsets.ModelViewSet):
    queryset = UseClientAquaAerobics.objects.order_by('-date')
    serializer_class = UseClientAquaAerobicsSerializer

    @list_route(methods=['post'], )
    def exit(self, request):
        aqua_id = request.data['client_aqua_aerobics']
        exit = UseClientAquaAerobics.objects\
                                    .filter(client_aqua_aerobics=aqua_id)\
                                    .update(end=datetime.now())
        return Response({'status': 'ok'}, status=status.HTTP_202_ACCEPTED)


class UseClientTicketViewSet(viewsets.ModelViewSet):
    queryset = UseClientTicket.objects.order_by('-date')
    serializer_class = UseClientTicketSerializer

    @list_route(methods=['post'], )
    def exit(self, request):
        ticket_id = request.data['client_ticket']
        exit = UseClientTicket.objects\
                              .filter(client_ticket=ticket_id)\
                              .update(end=datetime.now())
        return Response({'status': 'ok'}, status=status.HTTP_202_ACCEPTED)


class UseClientPersonalViewSet(viewsets.ModelViewSet):
    queryset = UseClientPersonal.objects.order_by('-date')
    serializer_class = UseClientPersonalSerializer

    @list_route(methods=['post'], )
    def exit(self, request):
        personal_id = request.data['client_personal']
        exit = UseClientPersonal.objects\
                                .filter(client_personal=personal_id)\
                                .update(end=datetime.now())
        return Response({'status': 'ok'}, status=status.HTTP_202_ACCEPTED)


class UseClientTimingViewSet(viewsets.ModelViewSet):
    queryset = UseClientTiming.objects.order_by('-date')
    serializer_class = UseClientTimingSerializer
