# -*- coding: utf-8 -*-
import ast

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

        for param in request.query_params:
            data = ast.literal_eval(request.query_params[param])
            field = data.get('search_object', '')
            text = data.get('search_text')
            if field in self.client_fields:
                filter_by = '%s__icontains' % field
                kwargs = {filter_by: text}
                queryset = queryset.filter(**kwargs)

        serializer = ClientSerializer(queryset, many=True)
        return Response(serializer.data)
