from rest_framework import viewsets

from .models import Position
from .serializers import PositionSerializer

class PositionViewSet(viewsets.ModelViewSet):
    queryset = Position.objects.order_by('name')
    serializer_class = PositionSerializer
