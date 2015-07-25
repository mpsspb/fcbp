# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response


def home(request, ):
    cont = dict(request=request, title='Главная', )
    return render_to_response('index.html', cont)