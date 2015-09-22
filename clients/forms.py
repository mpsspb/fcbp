# -*- coding: utf-8 -*-
from django.forms import ModelForm
from django import forms

from .models import ClientClubCard, ClientAquaAerobics
from .models import ClientTicket, ClientPersonal, ClientTiming


class FormClientClubCard(ModelForm):
    class Meta:
        model = ClientClubCard
        exclude = ['date', ]


class FormClientAquaAerobics(ModelForm):
    class Meta:
        model = ClientAquaAerobics
        exclude = ['date', ]


class FormClientTicket(ModelForm):
    class Meta:
        model = ClientTicket
        exclude = ['date', ]


class FormClientPersonal(ModelForm):
    class Meta:
        model = ClientPersonal
        exclude = ['date', ]


class FormClientTiming(ModelForm):
    class Meta:
        model = ClientTiming
        exclude = ['date', ]
