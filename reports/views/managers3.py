# -*- coding: utf-8 -*-
from datetime import timedelta, datetime

from django.utils.translation import ugettext as _

from reports import styles
from clients.models import (
    ProlongationClubCard, UseClientClubCard, ClubCardTrains)
from .base import ReportTemplate, Report


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


class VisitsPeriod(Report):
    file_name = 'club_card_visits'
    sheet_name = 'report'

    table_headers = [
        (_('date'), 4000),
        (_('gym'), 6000),
        (_('shaping'), 6000),
        (_('other group workouts'), 6000),
    ]

    def initial(self, request, *args, **kwargs):
        super(VisitsPeriod, self).initial(request, *args, **kwargs)
        self.total_gym = 0
        self.total_shaping = 0
        self.total_other = 0

    def get_title(self, **kwargs):
        return _("Attendance on club cards for the period").capitalize()

    def write_title(self):
        super(VisitsPeriod, self).write_title()
        msg = _('from: {fdate} to {tdate}')
        fdate = self.get_fdate().strftime('%d.%m.%Y')
        tdate = self.get_tdate().strftime('%d.%m.%Y')
        msg = msg.format(fdate=fdate, tdate=tdate)
        self.ws.write_merge(1, 1, 0, 3, msg, styles.styleh)

    def get_data(self):
        rows = []
        days = (self.get_tdate() - self.get_fdate()).days + 1
        for d in (self.get_fdate() + timedelta(n) for n in range(days)):
            line = []
            df = d.replace(hour=0, minute=0, second=0)
            dt = d.replace(hour=23, minute=59, second=59)
            line.append(d.strftime('%d.%m.%Y'))
            d_visits = UseClientClubCard.objects.filter(date__range=(df, dt))
            workout = ClubCardTrains.objects.filter(visit__in=d_visits)
            gym = workout.filter(training__order_num=0).count()
            shaping = workout.filter(training__order_num=1).count()
            other = workout.filter(training__order_num__gt=1).count()
            self.total_gym += gym
            self.total_shaping += shaping
            self.total_other += other
            line.append(gym)
            line.append(shaping)
            line.append(other)
            rows.append(line)
        line = [
            _("total"), self.total_gym, self.total_shaping, self.total_other]
        rows.append(line)
        return rows

    def write_bottom(self):
        total = self.total_gym + self.total_shaping + self.total_other
        self.ws.write(self.row_num, 0, _('total for period'))
        self.ws.write(self.row_num, 1, total, styles.styleh)
