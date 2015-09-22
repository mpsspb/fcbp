# -*- coding: utf-8 -*-
from django.forms import ModelForm
from django import forms

from .models import Credit, Payment


class FormCredit(ModelForm):
    class Meta:
        model = Credit
        exclude = ['date', ]


class FormPayment(ModelForm):
    class Meta:
        model = Payment
        exclude = ['date', ]
