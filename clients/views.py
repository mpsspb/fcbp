import json

from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.decorators import list_route
from rest_framework.pagination import PageNumberPagination

from .models import Client
from .serializers import ClientSerializer


class ClientResultsSetPagination(PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page_size'
    max_page_size = 10000


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects\
                     .order_by('last_name', 'first_name', 'patronymic')
    serializer_class = ClientSerializer
    pagination_class = ClientResultsSetPagination

