import json

from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.decorators import detail_route

from .models import Period, ClubCard
from .serializers import PeriodSerializer, ClubCardSerializer


class PeriodViewSet(viewsets.ModelViewSet):
    queryset = Period.objects.order_by('value')
    serializer_class = PeriodSerializer


class ClubCardViewSet(viewsets.ModelViewSet):
    queryset = ClubCard.objects.order_by('name')
    serializer_class = ClubCardSerializer
