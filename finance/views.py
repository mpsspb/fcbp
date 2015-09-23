from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import detail_route, list_route

from .models import Credit, Payment
from .serializers import CreditSerializer, PaymentSerializer


class CreditViewSet(viewsets.ModelViewSet):
    queryset = Credit.objects.order_by('-date')
    serializer_class = CreditSerializer

    @detail_route(methods=['post'])
    def close(self, request, pk):
        credit = self.get_object()
        pay_data = self.get_serializer(credit).data.copy()
        pay_data['payment_type'] = request.data['payment_type']
        del pay_data['id']
        serializer = PaymentSerializer(data=pay_data)
        if serializer.is_valid():
            serializer.save()
            credit.delete()
            return Response({'Credit': 'Is closed'},
                            status=status.HTTP_202_ACCEPTED)
        else:
            return Response(serializer.errors,
                            status=status.HTTP_406_NOT_ACCEPTABLE)


class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.order_by('-date')
    serializer_class = PaymentSerializer
