from datetime import datetime

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import list_route, detail_route

from fcbp.views import ActiveModel
from .models import *
from .serializers import *


class PositionViewSet(viewsets.ModelViewSet):
    queryset = Position.objects.order_by('name')
    serializer_class = PositionSerializer


class EmployeeViewSet(ActiveModel, viewsets.ModelViewSet):
    queryset = Employee.objects.filter(
        is_active=True).order_by('-is_active', 'last_name')
    full_list = Employee.objects.all().order_by('-is_active', 'last_name')
    serializer_class = EmployeeSerializer

    @list_route(methods=['get'], )
    def sellers(self, request):
        """
        Only employees who is seller.
        """
        queryset = self.queryset.filter(is_seller=True, is_active=True)
        serializer = EmployeeSerializer(queryset, many=True)
        return Response(serializer.data)

    @list_route(methods=['get'], )
    def personal_trainers(self, request):
        """
        Only employees who can do personals for current type.
        """
        positions = request.GET.get('positions', [])
        print (positions)
        now = datetime.now()
        filter_position = dict(date_begin__lte=now, date_end__isnull=True)
        epositions = EmployeePosition.objects.filter(**filter_position)
        emp_pks = epositions.values_list('employee__pk', flat=True)
        queryset = self.queryset.filter(pk__in=emp_pks, is_active=True)
        serializer = EmployeeSerializer(queryset, many=True)
        return Response(serializer.data)

    @detail_route(methods=['post', 'get'], )
    def active(self, request, pk,):
        self.queryset = self.full_list
        return super(EmployeeViewSet, self).active(request, pk,)

    @list_route(methods=['get'], )
    def all(self, request):
        serializer = EmployeeSerializer(self.full_list, many=True)
        return Response(serializer.data)
