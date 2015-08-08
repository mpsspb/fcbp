import json

from rest_framework import status, viewsets
from rest_framework.response import Response

from .models import Client
from .serializers import ClientSerializer


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects\
                     .order_by('last_name', 'first_name', 'patronymic')
    serializer_class = ClientSerializer
