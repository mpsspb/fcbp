from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.decorators import detail_route

from .models import *
from .serializers_archive import *


class ClientClubCardViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ClientClubCard.objects.order_by('-date')
    serializer_class = ClientClubCardSerializer

    @detail_route(methods=['get'], )
    def client(self, request, pk):
        """
        Get list archive club card for the client.
        """
        client = Client.objects.get(pk=pk)
        queryset = ClientClubCard.objects.filter(client=client)\
                                         .order_by('-date')
        serializer = ClientClubCardSerializer(queryset, many=True)
        return Response(serializer.data,
                        status=status.HTTP_202_ACCEPTED)


class ClientAquaAerobicsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ClientAquaAerobics.objects.order_by('-date')
    serializer_class = ClientAquaAerobicsSerializer

    @detail_route(methods=['get'], )
    def client(self, request, pk):
        """
        Get list archive aqua for the client.
        """
        client = Client.objects.get(pk=pk)
        queryset = ClientAquaAerobics.objects.filter(client=client)\
                                             .order_by('-date')
        serializer = ClientAquaAerobicsSerializer(queryset, many=True)
        return Response(serializer.data,
                        status=status.HTTP_202_ACCEPTED)
