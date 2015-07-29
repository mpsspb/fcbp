import json

from rest_framework import status, viewsets
from rest_framework.response import Response

from .models import Period
from .serializers import PeriodSerializer


class PeriodViewSet(viewsets.ModelViewSet):
    queryset = Period.objects.order_by('value')
    serializer_class = PeriodSerializer
