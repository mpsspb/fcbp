# -*- coding: utf-8 -*-
from datetime import datetime, timedelta

from django.shortcuts import render_to_response
from django.core.context_processors import csrf
from django.views.generic import View
from django.views.generic.edit import UpdateView

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
        pay_data['date'] = None
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

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        amount = int(request.data.get('amount', 0))
        if amount and amount > instance.amount:
            return Response({'error': u'Неверная сумма'},
                   status.HTTP_406_NOT_ACCEPTABLE)
        elif amount and amount < instance.amount:
            instance.split(amount)
            instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data,
                                         partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.order_by('-date')
    serializer_class = PaymentSerializer


class PaymentDateUpdate(UpdateView):
    template_name = 'finance/finance_form.html'
    model = Payment
    fields = ['date', 'payment_type']

    def get_success_url(self):
        return '/finance/'


class PaymentAmountUpdate(UpdateView):
    template_name = 'finance/finance_form.html'
    model = Payment
    fields = ['amount']

    def get_success_url(self):
        return '/finance/'

    def post(self, request, *args, **kwargs):
        data = self.request.POST.copy()
        payment = self.get_object()
        payment.split(data.get('amount'))
        resp = super(PaymentAmountUpdate, self).post(request, *args, **kwargs)
        return resp


class home(View, ):
    template_name = 'finance/finance.html'

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = request.POST.copy()
        fdate = data.get('fdate')
        if not fdate:
            fdate = datetime.now()-timedelta(7)
        else:
            fdate = datetime.strptime(fdate, '%d.%m.%Y %H:%M')
        tdate = data.get('tdate')
        if not tdate:
            tdate = datetime.now()
        else:
            tdate = datetime.strptime(tdate, '%d.%m.%Y %H:%M')
        payments = Payment.objects.filter(date__range=(fdate, tdate))
        cont = dict(
            request=request, title='Платежи', fdate=fdate, tdate=tdate,
            payments=payments.order_by('date'))
        cont.update(csrf(request))
        return render_to_response(self.template_name, cont)
