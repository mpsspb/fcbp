import json

from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.decorators import detail_route

from .models import Client
from .serializers import ClientSerializer


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects\
                     .order_by('last_name', 'first_name', 'patronymic')
    serializer_class = ClientSerializer

    @detail_route(methods=['post'])
    def img(self, request, pk=None):
        print (request)
        return Response({'status': 'password set'})
