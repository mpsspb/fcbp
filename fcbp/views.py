# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response

from rest_framework.response import Response
from rest_framework.decorators import detail_route, list_route


def home(request, ):
    cont = dict(request=request, title='Главная', )
    return render_to_response('index.html', cont)


class ActiveModel(object):

    """
    active/deactive the objects.
    list active objects.
    """
    @detail_route(methods=['post', 'get'], )
    def active(self, request, pk,):
        obj = self.get_object()
        obj.is_active = not obj.is_active
        obj.save()
        serializer = self.serializer_class(obj)
        return Response(serializer.data)

    @list_route(methods=['get'])
    def active_list(self, request):
        queryset = self.filter_queryset(self.get_queryset())\
                       .filter(is_active=True)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
