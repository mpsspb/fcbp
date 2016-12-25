# -*- coding: utf-8 -*-
from django.views.generic import View
from django.shortcuts import render_to_response
from django.utils.translation import ugettext_lazy as _


class Home(View, ):
    template_name = 'reports/menu.html'

    def get(self, request, *args, **kwargs):
        cont = dict(request=request, title=_('Reports'),)
        return render_to_response(self.template_name, cont)