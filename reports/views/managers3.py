# -*- coding: utf-8 -*-
from datetime import timedelta, datetime

from django.utils.translation import ugettext as _

from reports import styles
from clients.models import ProlongationClubCard
from .base import ReportTemplate


class ExtrProlongation(ReportTemplate):
    file_name = 'prolongation_cards_for_the_period'
    sheet_name = 'report'
    tpl_path = 'xls_tpl/prolongation.xls'
    tpl_start_row = 4

    table_headers = [
        (_('client'), 8000),
        (_('club card period'), 6000),
        (_('tariff'), 3000),
        (_('paid date'), 4000),
        (_('paid'), 4000),
        (_('p_days'), 3000),
        (_('p_days'), 3000),
        (_('note'), 8000),
    ]

    def get_title(self, **kwargs):
        msg = _('prolongation card for period.')
        msg += _(' created at: {date}.')
        date = datetime.now().strftime('%d.%m.%Y %H:%M')
        return msg.format(date=date)

    def write_title(self):
        super(ExtrProlongation, self).write_title()
        msg = _('from: {fdate} to {tdate}')
        fdate = self.get_fdate().strftime('%d.%m.%Y')
        tdate = self.get_tdate().strftime('%d.%m.%Y')
        msg = msg.format(fdate=fdate, tdate=tdate)
        self.ws.write_merge(1, 1, 0, 5, msg, styles.styleh)

    def get_data(self):

        def join_list(l1, l2):
            result = []
            l1_len = len(l1)
            l2_len = len(l2)
            for i in range(max(l1_len, l2_len)):
                list_len = i + 1
                if l1_len >= list_len and l2_len >= list_len:
                    map_u = lambda x, y: unicode(x) + unicode(y)
                    join_l = map(map_u, l1[i], l2[i])
                elif l2_len >= list_len:
                    join_l = map(unicode, l2[i])
                else:
                    join_l = map(unicode, l1[i])
                result.append(join_l)
            return result

        rows = []
        cards = []
        line_paid = []
        line_extra = []
        fdate = self.get_fdate().date()
        tdate = self.get_tdate().date() + timedelta(1)
        data = ProlongationClubCard.objects.filter(date__range=(fdate, tdate))
        for row in data.order_by(
            'client_club_card__date_end', 'is_paid', '-date'):
            if not row.is_paid and not row.is_extra:
                next
            line = []
            card = row.parent
            if not card.pk in cards:
                if line_extra or line_paid:
                    for pr in join_list(line_extra, line_paid):
                        rows.append(pr)
                    line_paid = []
                    line_extra = []
                cards.append(card.pk)
                line.append(card.client.full_name)
                period_data = {
                    'bdate': card.date_begin.strftime('%d.%m.%Y'),
                    'edate': card.date_end.strftime('%d.%m.%Y')
                }
                period = '{bdate}-{edate}'.format(**period_data)
                line.append(period)
                line.append(card.short_name)
                rows.append(line)
            if row.is_paid:
                line_p = []
                line_p.extend(['', '', ''])
                line_p.append(row.date.strftime('%d.%m.%Y'))
                line_p.append(row.amount)
                line_p.append(row.days)
                line_p.extend(['', ''])
                line_paid.append(line_p)
            else:
                line_e = []
                line_e.extend(['', '', '', '', '', ''])
                line_e.append(row.days)
                line_e.append(row.note or '')
                line_extra.append(line_e)
        if line_extra or line_paid:
            for pr in join_list(line_extra, line_paid):
                rows.append(pr)
        return rows

    def write_bottom(self):
        pass