# -*- coding: utf-8 -*-
from datetime import timedelta, datetime

from django.utils.translation import ugettext as _
from django.db.models import Sum

from .base import ReportTemplate
from reports import styles
from clients.models import (
    ClientClubCard, UseClientClubCard, Client, ClubCardTrains)
from products.models import ClubCard
from finance.models import Payment


class ActiveClubCard(ReportTemplate):

    file_name = 'list_active_club_cards'
    sheet_name = 'report'
    tpl_path =  'xls_tpl/active_clubcard.xls'
    tpl_start_row = 7

    table_headers = [
        (_('client'), 4000),
        (_('club card'), 10000),
        (_('dates'), 4000),
        (_('use trainings'), 6000),
        (_('last visit'), 4000),
        (_('credits'), 4000),
        (_('freeze/prolongation'), 8000),
        (_('extra options'), 4000),
        (_('guest visit'), 4000),
    ]

    table_styles = {
        2: styles.styled,
    }

    def initial(self, request, *args, **kwargs):
        super(ActiveClubCard, self).initial(request, *args, **kwargs)
        clubcard_id = self.request.query_params.get('cc')
        self.clubcard = ClubCard.objects.get(pk=clubcard_id)

    def get_fdate(self):
        return datetime.now()

    def get_title(self, **kwargs):
        msg = _(
            'list active club cards')
        msg += _(' created at: {date}.')
        date = self.get_fdate().strftime('%d.%m.%Y %H:%M')
        return msg.format(date=date)

    def get_data(self):
        rows = []
        data = ClientClubCard.objects.filter(
            status=1, club_card=self.clubcard).order_by('pk')
        for row in data:
            line = []
            fname = row.client.first_name
            pname = row.client.patronymic
            lname = row.client.last_name
            uid = row.client.uid
            line.append((fname, pname, lname, uid))
            phone = row.client.mobile or row.client.phone or ''
            tariff = self.clubcard.short_name
            amount = row.summ_amount
            discount = row.discount_short
            line.append((phone, tariff, amount, discount))
            date_begin = row.date_begin.strftime('%d.%m.%Y')
            date_end = row.date_end.strftime('%d.%m.%Y')
            line.append((date_begin, date_end, '', ''))
            visits = row.useclientclubcard_set.all()
            training = ClubCardTrains.objects.filter(visit__in=visits).count()
            line.append((training, '', '', ''))
            if visits:
                last_visit = visits.last().date.strftime('%d.%m.%Y')
                line.append((last_visit, '', '', ''))
            else:
                line.append(('', '', '', ''))
            schedule = []
            for p in row.schedule_payments():
                if p[0] <= self.get_fdate():
                    continue
                pdate = p[0].strftime('%d.%m.%Y')
                pamount = "{:,}".format(p[1]).replace(',', ' ')
                schedule.append("%s - %s" % (pamount, pdate))
            schedule.extend([''] * (4 - len(schedule)))
            line.append(schedule)
            freeze = []
            use_freeze = row.freezeclubcard_set.all()
            for f in use_freeze.filter(is_extra=False, is_paid=False):
                freeze.append(f.days)
            use_prol = row.prolongationclubcard_set.all()
            for p in use_prol.filter(is_extra=False, is_paid=False):
                freeze.append(p.days)
            freeze.extend([''] * (4 - len(freeze)))
            line.append(freeze)
            fitness = row.fitnessclubcard_set.first()
            fitness = fitness.date.strftime('%d.%m.%Y') if fitness else ''
            personal = row.personalclubcard_set.first()
            personal = personal.date.strftime('%d.%m.%Y') if personal else ''
            line.append((personal, '', '', fitness))
            guests = []
            for guest in row.guestclubcard_set.all().order_by('date'):
                guests.append(guest.date.strftime('%d.%m.%Y'))
            guests.extend([''] * (4 - len(guests)))
            line.append(guests)
            rows.append(line)
        return rows

    def write_heads(self):
        super(ActiveClubCard, self).write_heads()
        self.ws.write(2, 2, self.clubcard.name, styles.styleh)


    def write_bottom(self):
        pass

