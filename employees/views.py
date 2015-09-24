from rest_framework import viewsets

from .models import *
from .serializers import *


class PositionViewSet(viewsets.ModelViewSet):
    queryset = Position.objects.order_by('name')
    serializer_class = PositionSerializer


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.order_by('last_name')
    serializer_class = EmployeeSerializer
