import json
from datetime import datetime, timedelta

from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.decorators import list_route, detail_route
from rest_framework.pagination import PageNumberPagination

from .models import *
from .forms import *
from .serializers import *
from .serializers_light import ClientClubCardSerial
from .use_serializers import *


class ClientResultsSetPagination(PageNumberPagination):
    page_size = 10000
    page_size_query_param = 'page_size'
    max_page_size = 10000


class ClientViewSet(viewsets.ModelViewSet):

    serializer_class = ClientSerializer
    pagination_class = ClientResultsSetPagination

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data,
                                         partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

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
        Search clients istartswith last_name, first_name and patronymic.
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

    @list_route(methods=['post'], )
    def exact_search(self, request):
        """
        Search clients iexact of last_name, first_name and patronymic.
        """
        last_name = request.data.get('last_name', None)
        if last_name:
            queryset = Client.objects.filter(last_name__iexact=last_name)
        first_name = request.data.get('first_name', None)
        if first_name:
            if last_name:
                queryset = queryset.filter(first_name__iexact=first_name)
            else:
                queryset = Client.objects.filter(last_name__iexact=first_name)
        patronymic = request.data.get('patronymic', None)
        if patronymic:
            if last_name or first_name:
                queryset = queryset.filter(patronymic__iexact=patronymic)
            else:
                queryset = Client.objects.filter(last_name__iexact=patronymic)
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

    @detail_route(methods=['get'], )
    def last_clubcard(self, request, pk):
        """
        Set introductory for the user.
        """
        client = self.get_object()
        queryset = ClientClubCard.objects.filter(client=client)\
                                         .order_by('-date')[:5]
        first = queryset[0]
        last = queryset[1:5]
        serializer_first = ClientClubCardSerial(first)
        serializer_last = ClientClubCardSerial(last, many=True)
        return Response({'first': serializer_first.data,
                         'last': serializer_last.data},
                        status=status.HTTP_202_ACCEPTED)


class ClientClubCardViewSet(viewsets.ModelViewSet):
    queryset = ClientClubCard.objects.order_by('-date')
    serializer_class = ClientClubCardSerializer

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data,
                                         partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    @detail_route(methods=['post'], )
    def guest(self, request, pk):
        """
        use free guest visit
        """
        data = request.data.copy()
        data['client_club_card'] = self.get_object().pk
        serializer = GuestClubCardSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,
                            status=status.HTTP_406_NOT_ACCEPTABLE)

    @detail_route(methods=['post'], )
    def freeze(self, request, pk):
        """
        freeze the card and update the date_end of the card.
        """
        data = request.data.copy()
        club_card = self.get_object()
        data['client_club_card'] = club_card.pk
        data['client'] = club_card.client.pk
        serializer = FreezeClubCardSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            date_end = club_card.date_end + timedelta(serializer.data['days'])
            club_card.date_end = date_end
            club_card.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,
                            status=status.HTTP_406_NOT_ACCEPTABLE)


class FitnessClubCardViewSet(viewsets.ModelViewSet):
    queryset = FitnessClubCard.objects.order_by('-date')
    serializer_class = FitnessClubCardSerializer


class PersonalClubCardViewSet(viewsets.ModelViewSet):
    queryset = PersonalClubCard.objects.order_by('-date')
    serializer_class = PersonalClubCardSerializer


class ProlongationClubCardViewSet(viewsets.ModelViewSet):
    queryset = ProlongationClubCard.objects.order_by('-date')
    serializer_class = ProlongationClubCardSerializer


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

    def create(self, request):
        """
        Comming client to the club and escape existing freeze.
        """
        data = request.data.copy()
        trainings = data.get('trainings', [])
        if len(trainings) < 1:
            return Response({'Error:': 'Empty trainings'},
                            status=status.HTTP_406_NOT_ACCEPTABLE)
        serializer = UseClientClubCardSerializer(data=data)
        if serializer.is_valid():
            obj = serializer.save()
            # save trainings
            for tr in trainings:
                ClubCardTrains.objects.create(visit_id=obj.pk,
                                              training_id=tr['id'])
            ucc = ClientClubCard.objects.get(pk=data['client_club_card'])
            if ucc.is_frozen:
                ucc.escape_frozen()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,
                            status=status.HTTP_406_NOT_ACCEPTABLE)

    @list_route(methods=['post'], )
    def exit(self, request):
        card_id = request.data['client_club_card']
        exit = UseClientClubCard.objects\
                                .filter(client_club_card=card_id,
                                        end=None)\
                                .update(end=datetime.now())
        return Response({'status': 'ok'}, status=status.HTTP_202_ACCEPTED)


class UseClientAquaAerobicsViewSet(viewsets.ModelViewSet):
    queryset = UseClientAquaAerobics.objects.order_by('-date')
    serializer_class = UseClientAquaAerobicsSerializer

    @list_route(methods=['post'], )
    def exit(self, request):
        aqua_id = request.data['client_aqua_aerobics']
        exit = UseClientAquaAerobics.objects\
                                    .filter(client_aqua_aerobics=aqua_id,
                                            end=None)\
                                    .update(end=datetime.now())
        return Response({'status': 'ok'}, status=status.HTTP_202_ACCEPTED)


class UseClientTicketViewSet(viewsets.ModelViewSet):
    queryset = UseClientTicket.objects.order_by('-date')
    serializer_class = UseClientTicketSerializer

    @list_route(methods=['post'], )
    def exit(self, request):
        ticket_id = request.data['client_ticket']
        exit = UseClientTicket.objects\
                              .filter(client_ticket=ticket_id,
                                      end=None)\
                              .update(end=datetime.now())
        return Response({'status': 'ok'}, status=status.HTTP_202_ACCEPTED)


class UseClientPersonalViewSet(viewsets.ModelViewSet):
    queryset = UseClientPersonal.objects.order_by('-date')
    serializer_class = UseClientPersonalSerializer

    @list_route(methods=['post'], )
    def exit(self, request):
        personal_id = request.data['client_personal']
        exit = UseClientPersonal.objects\
                                .filter(client_personal=personal_id,
                                        end=None)\
                                .update(end=datetime.now())
        return Response({'status': 'ok'}, status=status.HTTP_202_ACCEPTED)


class UseClientTimingViewSet(viewsets.ModelViewSet):
    queryset = UseClientTiming.objects.order_by('-date')
    serializer_class = UseClientTimingSerializer
