import json

from rest_framework import status, viewsets
from rest_framework.response import Response

from .models import Period, ClubCard, AquaAerobics, Sport, Ticket, Personal
from .serializers import PeriodSerializer, ClubCardSerializer
from .serializers import AquaAerobicsSerializer, SportSerializer
from .serializers import TicketSerializer, PersonalSerializer


class PeriodViewSet(viewsets.ModelViewSet):
    queryset = Period.objects.order_by('value')
    serializer_class = PeriodSerializer


class ClubCardViewSet(viewsets.ModelViewSet):
    queryset = ClubCard.objects.order_by('name')
    serializer_class = ClubCardSerializer


class AquaAerobicsViewSet(viewsets.ModelViewSet):
    queryset = AquaAerobics.objects.order_by('name')
    serializer_class = AquaAerobicsSerializer


class SportViewSet(viewsets.ModelViewSet):
    queryset = Sport.objects.order_by('name')
    serializer_class = SportSerializer


class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.order_by('name')
    serializer_class = TicketSerializer


class PersonaViewSet(viewsets.ModelViewSet):
    queryset = Personal.objects.order_by('name')
    serializer_class = PersonalSerializer
