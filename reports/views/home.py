# -*- coding: utf-8 -*-
from django.views.generic import View
from django.shortcuts import render_to_response
from django.utils.translation import ugettext_lazy as _

from clients.models import ClientClubCard


class Home(View, ):
    template_name = 'reports/menu.html'

    def get(self, request, *args, **kwargs):
        cc = ClientClubCard.objects.filter(status=1)
        cc_options = cc.values(
            'club_card__name', 'club_card__pk'
        ).order_by('club_card__name').distinct()
        cont = dict(
            request=request, title=_('Reports'), cc_options=cc_options)
        return render_to_response(self.template_name, cont)


class Reception(View, ):
    template_name = 'reports/reception_menu.html'

    def get(self, request, *args, **kwargs):
        cont = dict(request=request, title=_('Reports'))
        return render_to_response(self.template_name, cont)
