import json

from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.decorators import list_route

from .models import Client
from .serializers import ClientSerializer


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects\
                     .order_by('last_name', 'first_name', 'patronymic')
    serializer_class = ClientSerializer

    @list_route(methods=['get'])
    def letter(self, request):
        pass
        # print (request)
        # letter = request.GET.get('letter', None)
        # queryset = Client.objects\
        #                  .filter(last_name__istartwith=letter)\
        #                  .order_by('last_name', 'first_name', 'patronymic')

        # serializer = ClientSerializer(queryset, many=True)

        # return Response(serializer.data)
