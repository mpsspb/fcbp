# -*- coding: utf-8 -*-
from datetime import timedelta

from django.utils.translation import ugettext as _

from reports import styles
from finance.models import Payment
from clients.models import ClientClubCard
from products.models import Period, ClubCard
from .base import ReportTemplate


class TotalClubCard(ReportTemplate):

    file_name = 'total_club_cards'
    sheet_name = 'total_club_cards'
    tpl_path = 'xls_tpl/total_cards.xls'
    tpl_start_row = 3

    table_headers = [
        (_('total'), 4000),
        (_('club card'), 10000), ]

    def initial(self, request, *args, **kwargs):
        super(TotalClubCard, self).initial(request, *args, **kwargs)
        self.total = 0
        self.total_limit = 0
        self.total_full = 0
        self.periods = {}

    def get_title(self, **kwargs):
        return _('total club cards')

    def write_title(self):
        super(TotalClubCard, self).write_title()
        msg = _('from: {fdate} to {tdate}')
        fdate = self.get_fdate().strftime('%d.%m.%Y')
        tdate = self.get_tdate().strftime('%d.%m.%Y')
        msg = msg.format(fdate=fdate, tdate=tdate)
        self.ws.write_merge(1, 1, 0, 5, msg, styles.styleh)

    def get_data(self):
        rows = []
        cards = []
        fdate = self.get_fdate().date()
        tdate = self.get_tdate().date() + timedelta(1)
        payments = Payment.objects.filter(
            date__range=(fdate, tdate)
        ).exclude(club_card__isnull=True)
        for p in payments:
            if p.club_card.first_payment == p:
                cards.append(p.club_card.pk)
        data = ClientClubCard.objects.filter(pk__in=cards)
        data = data.order_by(
            'club_card__period__is_month',
            'club_card__period__value',
            'club_card__name')
        data = data.values_list('club_card__pk', flat=True).distinct()
        for row in range(0, len(data)/3 + 1):
            line = []
            for cc in data[row * 3: (row + 1) * 3]:
                club_card = ClubCard.objects.get(pk=cc)
                line.append(club_card.short_name)
                cnt = ClientClubCard.objects.filter(
                    pk__in=cards, club_card=club_card).count()
                line.append(cnt)
                self.total += cnt
                if club_card.is_full_time:
                    self.total_full += cnt
                if club_card.max_visit < 99999:
                    self.total_limit += cnt
                if club_card.period.pk not in self.periods:
                    self.periods[club_card.period.pk] = cnt
                else:
                    self.periods[club_card.period.pk] += cnt
            rows.append(line)
        return rows

    def write_heads(self):
        pass

    def write_bottom(self):
        self.ws.write(self.row_num, 0, _('total'))
        self.ws.write(self.row_num, 1, self.total, styles.styleh)
        self.row_num += 1
        self.ws.write(self.row_num, 0, _('including:'))
        self.row_num += 1
        self.ws.write(self.row_num, 0, _('limited'), styles.styleth)
        self.ws.write(self.row_num, 1, self.total_limit, styles.styleth)
        self.ws.write(self.row_num, 3, _('UBV'), styles.style)
        ubv_cnt = self.total - self.total_full
        self.ws.write(self.row_num, 4, ubv_cnt, styles.style)
        self.row_num += 1
        periods = Period.objects.filter(
            pk__in=self.periods).order_by('is_month', 'value')
        if periods:
            period = periods[0]
            self.ws.write(self.row_num, 0,period.name, styles.styleth)
            self.ws.write(
                self.row_num, 1, self.periods[period.pk], styles.styleth)
        self.ws.write(self.row_num, 3, _('P'), styles.style)
        self.ws.write(self.row_num, 4, self.total_full, styles.style)
        for period in periods[1:]:
            self.row_num += 1
            self.ws.write(self.row_num, 0,period.name, styles.styleth)
            self.ws.write(
                self.row_num, 1, self.periods[period.pk], styles.styleth)
