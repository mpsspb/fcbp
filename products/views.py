import json

from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.decorators import detail_route, list_route

from .models import Period, ClubCard, AquaAerobics, Sport, Ticket
from .models import Personal, PersonalPosition, Timing
from .serializers import PeriodSerializer, ClubCardSerializer
from .serializers import AquaAerobicsSerializer, SportSerializer
from .serializers import TicketSerializer, PersonalSerializer
from .serializers import PersonalPositionSerializer, TimingSerializer


class ActiveModel(object):
    """
    active/deactive the clubcard.
    """
    @detail_route(methods=['post', 'get'], )
    def active(self, request, pk,):
        obj = self.get_object()
        obj.is_active = not obj.is_active
        obj.save()
        serializer = self.serializer_class(obj)
        return Response(serializer.data)


class PeriodViewSet(viewsets.ModelViewSet):
    queryset = Period.objects.order_by('value')
    serializer_class = PeriodSerializer


class ClubCardViewSet(viewsets.ModelViewSet, ActiveModel):
    queryset = ClubCard.objects.order_by('name')
    serializer_class = ClubCardSerializer


class AquaAerobicsViewSet(viewsets.ModelViewSet, ActiveModel):
    queryset = AquaAerobics.objects.order_by('name')
    serializer_class = AquaAerobicsSerializer


class SportViewSet(viewsets.ModelViewSet):
    queryset = Sport.objects.order_by('name')
    serializer_class = SportSerializer


class TicketViewSet(viewsets.ModelViewSet, ActiveModel):
    queryset = Ticket.objects.order_by('name')
    serializer_class = TicketSerializer


class PersonalViewSet(viewsets.ModelViewSet, ActiveModel):
    queryset = Personal.objects.order_by('name')
    serializer_class = PersonalSerializer


class PersonalPositionViewSet(viewsets.ModelViewSet):
    queryset = PersonalPosition.objects.all()
    serializer_class = PersonalPositionSerializer


class TimingViewSet(viewsets.ModelViewSet, ActiveModel):
    queryset = Timing.objects.order_by('name')
    serializer_class = TimingSerializer
