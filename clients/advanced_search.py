# -*- coding: utf-8 -*-
from datetime import datetime

from rest_framework import viewsets
from rest_framework.response import Response

from .models import Client
from .serializers import ClientSerializer


class ClientSearchViewSet(viewsets.ViewSet):
    """
    Advabce clients search by parameters.
    """
    client_fields = ['last_name', 'first_name', 'patronymic', 'uid']

    def list(self, request, ):
        """
        Optionally restricts the returned clients,
        by filtering against a `letter` query parameter in the URL.
        """
        queryset = Client.objects\
                         .order_by('last_name', 'first_name', 'patronymic')

        filter_str = ('%s__icontains', '%s__istartswith', '%s__iexact')
        data = request.query_params
        field = data.get('search_object', '')
        text = data.get('search_text')
        comparison = data.get('comparison', 0)
        try:
            comparison = int(comparison)
            comparison = filter_str[comparison]
        except Exception:
            comparison = filter_str[0]
        if field in self.client_fields:
            filter_by = comparison % field
            kwargs = {filter_by: text}
            queryset = queryset.filter(**kwargs)
        elif field == 'fio':
            fio_filds = ('last_name', 'first_name', 'patronymic')
            search_text = text.split()
            for i, fio in enumerate(search_text):
                filter_by = comparison % fio_filds[i]
                kwargs = {filter_by: fio}
                queryset = queryset.filter(**kwargs)
        elif field == 'born':
            born = datetime.strptime(text, "%d.%m.%Y").date()
            queryset = queryset.filter(born=born)

        serializer = ClientSerializer(queryset, many=True)
        return Response(serializer.data)
