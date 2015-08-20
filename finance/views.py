from rest_framework import viewsets

from .models import Credit
from .serializers import CreditSerializer


class CreditViewSet(viewsets.ModelViewSet):
    queryset = Credit.objects.order_by('-date')
    serializer_class = CreditSerializer
