# -*- coding: utf-8 -*-
from datetime import timedelta, datetime

from django.utils.translation import ugettext as _

from reports import styles
from clients.models import (
    ProlongationClubCard, UseClientClubCard, ClubCardTrains, ClientClubCard)
from finance.models import Payment
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
        rows = []
        fdate = self.get_fdate().date()
        tdate = self.get_tdate().date() + timedelta(1)
        club_cards = ProlongationClubCard.objects.filter(
            date__range=(fdate, tdate)).values('client_club_card')
        data = ClientClubCard.objects.filter(pk__in=club_cards)
        for row in data.order_by('date_end'):
            line = []
            card = row
            ext_prolongation = card.ext_prolongation()
            if not ext_prolongation:
                continue
            line.append(card.client.full_name)
            period_data = {
                'bdate': card.date_begin.strftime('%d.%m.%Y'),
                'edate': card.date_end.strftime('%d.%m.%Y')
            }
            period = '{bdate}-{edate}'.format(**period_data)
            line.append(period)
            line.append(card.short_name)
            line.append(ext_prolongation)
            rows.append(line)
        return rows

    def write_data(self):
        for row in self.get_data():
            row_step = len(row[3]) - 1
            for i, cell in enumerate(row[:3]):
                style = self.table_styles.get(i, styles.style_c)
                bottom_row = self.row_num + row_step
                self.ws.write_merge(
                    self.row_num, bottom_row, i, i,
                    cell, style)
                for si, sub_row in enumerate(row[3]):
                    for y, sub_cell in enumerate(sub_row):
                        rnum = self.row_num + si
                        cnum = y + 3
                        self.ws.write(rnum, cnum, sub_cell, style)
            self.row_num += (1 + row_step)

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


class OtherPayments(Report):
    """docstring for OtherPayments"""
    file_name = 'club_card_otherpayments'
    sheet_name = 'report'

    table_headers = [
        (_('client'), 8000),
        (_('paid date'), 3000),
        (_('co number'), 4000),
        (_('club card num'), 4000),
        (_('tariff'), 6000),
        (_('total paid'), 4000),
        (_('other paid'), 4000),
        (_('seller'), 6000),
        (_('document for other paid'), 6000),
    ]

    table_styles = {
        1: styles.styled,
    }

    def get_title(self, **kwargs):
        return _("other paid report").capitalize()

    def write_title(self):
        super(OtherPayments, self).write_title()
        msg = _('from: {fdate} to {tdate}')
        fdate = self.get_fdate().strftime('%d.%m.%Y')
        tdate = self.get_tdate().strftime('%d.%m.%Y')
        msg = msg.format(fdate=fdate, tdate=tdate)
        ln_head = len(self.table_headers) - 1
        self.ws.write_merge(1, 1, 0, ln_head, msg, styles.styleh)

    def get_data(self):
        rows = []
        fdate = self.get_fdate().date()
        end_date = self.get_tdate() + timedelta(1)
        data = Payment.objects.filter(
            date__range=(fdate, end_date)
        ).exclude(club_card__isnull=True).filter(payment_type=3)
        for row in data:
            if row.extra_uid:
                continue
            line = []
            card = row.club_card
            line.append(row.client.full_name)
            line.append(row.date)
            line.append(row.client.uid)
            line.append(row.client.card)
            line.append(row.goods_short_name())
            line.append(card.summ_amount)
            line.append(row.amount)
            employee = card.employee.full_name if card.employee else ''
            line.append(employee)
            line.append('')
            rows.append(line)
        return rows

    def write_bottom(self):
        pass
