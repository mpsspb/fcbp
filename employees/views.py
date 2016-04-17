from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import list_route

from .models import *
from .serializers import *


class PositionViewSet(viewsets.ModelViewSet):
    queryset = Position.objects.order_by('name')
    serializer_class = PositionSerializer


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.order_by('last_name')
    serializer_class = EmployeeSerializer

    @list_route(methods=['get'], )
    def sellers(self, request):
        """
        Only employees who is seller.
        """
        queryset = self.queryset.filter(is_seller=True)
        serializer = EmployeeSerializer(queryset, many=True)
        return Response(serializer.data)
