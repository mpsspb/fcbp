# -*- coding: utf-8 -*-
from collections import defaultdict
from datetime import timedelta, datetime

from django.utils.translation import ugettext as _

from reports import styles
from finance.models import Payment
from clients.models import ClientClubCard
from products.models import Period, ClubCard, Discount
from .base import ReportTemplate, Report


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
            self.ws.write(self.row_num, 0, period.name, styles.styleth)
            self.ws.write(
                self.row_num, 1, self.periods[period.pk], styles.styleth)
        self.ws.write(self.row_num, 3, _('P'), styles.style)
        self.ws.write(self.row_num, 4, self.total_full, styles.style)
        for period in periods[1:]:
            self.row_num += 1
            self.ws.write(self.row_num, 0, period.name, styles.styleth)
            self.ws.write(
                self.row_num, 1, self.periods[period.pk], styles.styleth)


class ClubCardDiscount(Report):

    file_name = 'club_cards_discounts'
    sheet_name = 'club_cards_discounts'

    table_headers = [
        (_('client'), 10000),
        (_('# uid'), 6000),
        (_('tariff'), 6000),
        (_('paid date'), 6000),
        (_('discount type'), 4000),
        (_('discount'), 6000),
    ]

    table_styles = {
        1: styles.style_c,
        2: styles.style_c,
        3: styles.styled,
        4: styles.style_c,
        5: styles.style_c,
    }

    def initial(self, request, *args, **kwargs):
        super(ClubCardDiscount, self).initial(request, *args, **kwargs)
        self.total = {}

    def get_title(self, **kwargs):
        return _('club cards discounts')

    def write_title(self):
        super(ClubCardDiscount, self).write_title()
        msg = _('from: {fdate} to {tdate}')
        fdate = self.get_fdate().strftime('%d.%m.%Y')
        tdate = self.get_tdate().strftime('%d.%m.%Y')
        msg = msg.format(fdate=fdate, tdate=tdate)
        heads_ln = len(self.table_headers)
        self.ws.write_merge(1, 1, 0, heads_ln, msg, styles.styleh)

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
        discounts = ClientClubCard.objects.filter(
            pk__in=cards, discount_amount__gt=0)
        bonus = ClientClubCard.objects.filter(
            pk__in=cards, bonus_amount__gt=0)
        data = discounts | bonus
        data = data.distinct()
        for row in data:
            line = []
            line.append(row.client.full_name)
            line.append(row.client.uid)
            line.append(row.club_card.short_name)
            line.append(row.first_payment.date)
            line.append(row.discount_short)
            if row.discount_short not in self.total:
                self.total[row.discount_short] = 1
            else:
                self.total[row.discount_short] += 1
            discount_value = row.discount_value
            if discount_value <= 100:
                discount_value = ('{value} %').format(value=discount_value)
            line.append(discount_value)
            rows.append(line)
        return sorted(rows, key=lambda row: row[3])

    def write_bottom(self):
        self.ws.write(self.row_num, 0, _('total'))
        for row in sorted(self.total.items(), key=lambda t: t[0]):
            self.ws.write(self.row_num, 1, row[0], styles.style_c)
            self.ws.write(self.row_num, 2, row[1], styles.style_c)
            self.row_num += 1


class ClubCardDisabled(Report):

    file_name = 'club_cards_disabled'
    sheet_name = 'club_cards_disabled'

    table_headers = [
        (_('create date'), 4000),
        (_('client'), 8000),
        (_('# uid'), 4000),
        (_('club card period'), 6000),
        (_('tariff'), 4000),
        (_('reason for blocking'), 6000),
    ]

    table_styles = {
        0: styles.styled,
        1: styles.style_c,
        2: styles.style_c,
        3: styles.style_c,
    }

    def initial(self, request, *args, **kwargs):
        super(ClubCardDisabled, self).initial(request, *args, **kwargs)
        self.total = 0

    def get_title(self, **kwargs):
        return _('blocked cards during the period')

    def write_title(self):
        super(ClubCardDisabled, self).write_title()
        msg = _('from: {fdate} to {tdate}')
        fdate = self.get_fdate().strftime('%d.%m.%Y')
        tdate = self.get_tdate().strftime('%d.%m.%Y')
        msg = msg.format(fdate=fdate, tdate=tdate)
        heads_ln = len(self.table_headers)
        self.ws.write_merge(1, 1, 0, heads_ln, msg, styles.styleh)

    def get_data(self):
        rows = []
        fdate = self.get_fdate().date()
        tdate = self.get_tdate().date() + timedelta(1)
        data = ClientClubCard.objects.filter(
            date_end__range=(fdate, tdate), status=0).order_by('-date')
        for row in data:
            line = []
            line.append(row.date)
            line.append(row.client.full_name)
            line.append(row.client.uid)
            period_data = {
                'bdate': row.date_begin.strftime('%d.%m.%Y'),
                'edate': row.date_end.strftime('%d.%m.%Y')
            }
            period = '{bdate}-{edate}'.format(**period_data)
            line.append(period)
            line.append(row.club_card.short_name)
            line.append(row.block_comment)
            rows.append(line)
        self.total = len(rows)
        return rows

    def write_bottom(self):
        self.ws.write(self.row_num, 0, _('total'), styles.styleh)
        self.ws.write(self.row_num, 1, _('all locked cards'), styles.styleh)
        self.ws.write(self.row_num, 2, self.total, styles.styleh)


class ClubCardProspect(Report):

    file_name = 'club_cards_prospect'
    sheet_name = 'club_cards_prospect'

    table_headers = [
        (_('paid date'), 4000),
        (_('client'), 8000),
        (_('# uid'), 4000),
        (_('club card num'), 4000),
        (_('tariff'), 4000),
    ]

    table_styles = {
        0: styles.styled,
        1: styles.style_c,
        2: styles.style_c,
        3: styles.style_c,
    }

    def initial(self, request, *args, **kwargs):
        super(ClubCardProspect, self).initial(request, *args, **kwargs)
        self.total = 0

    def get_title(self, **kwargs):
        msg = _('not activated the card to date')
        msg += _(' created at: {date}.')
        tdate = self.get_fdate().strftime('%d.%m.%Y %H:%M')
        return msg.format(date=tdate)

    def get_fdate(self):
        return datetime.now()

    def get_data(self):
        rows = []
        data = ClientClubCard.objects.filter(
            date_begin__isnull=True, status__gt=0).order_by('-date')
        for row in data:
            line = []
            line.append(row.first_payment.date)
            line.append(row.client.full_name)
            line.append(row.client.uid)
            line.append(row.client.card)
            line.append(row.club_card.short_name)
            rows.append(line)
        self.total = len(rows)
        return rows

    def write_bottom(self):
        self.ws.write(self.row_num, 0, _('total'), styles.styleh)
        self.ws.write(self.row_num, 1, _('all inactive cards'), styles.styleh)
        self.ws.write(self.row_num, 2, self.total, styles.styleh)


class BestLoyalty(Report):

    file_name = 'club_cards_best_loyalty'
    sheet_name = 'club_cards_best_loyalty'

    table_headers = [
        (_('client'), 8000),
        (_('# uid'), 4000),
        (_('previous tariff'), 4000),
        (_('new tariff'), 4000),
        (_('previous date end'), 4000),
        (_('new date end'), 4000),
        (_('previous discount'), 4000),
        (_('new discount'), 4000),
        (_('new paid date'), 4000),
    ]

    table_styles = {
        0: styles.style_c,
        1: styles.style_c,
        2: styles.style_c,
        3: styles.style_c,
        6: styles.style_c,
        7: styles.style_c,
    }

    def initial(self, request, *args, **kwargs):
        super(BestLoyalty, self).initial(request, *args, **kwargs)
        self.total = 0
        self.discounts = defaultdict(int)
        self.red_font = styles.style_red_font
        self.red_font.borders = styles.borders
        self.red_font.alignment = styles.alignment_c

    def get_title(self, **kwargs):
        return _('sales at best loyalty')

    def write_title(self):
        super(BestLoyalty, self).write_title()
        msg = _('from: {fdate} to {tdate}')
        fdate = self.get_fdate().strftime('%d.%m.%Y')
        tdate = self.get_tdate().strftime('%d.%m.%Y')
        msg = msg.format(fdate=fdate, tdate=tdate)
        heads_ln = len(self.table_headers)
        self.ws.write_merge(1, 1, 0, heads_ln, msg, styles.styleh)

    def get_data(self):
        rows = []
        bl_discounts = Discount.objects.filter(is_best_loyalty=True)
        fdate = self.get_fdate().date()
        tdate = self.get_tdate().date() + timedelta(1)
        data = ClientClubCard.objects.filter(
            discount_type__in=bl_discounts, date__range=(fdate, tdate)
            ).order_by('date')
        for row in data:
            line = []
            previous_card = row.previous_card()
            line.append(row.client.full_name)
            line.append(row.client.uid)
            if previous_card:
                line.append(previous_card.club_card.short_name)
            else:
                line.append('')
            line.append(row.club_card.short_name)
            if previous_card:
                line.append(previous_card.date_end)
            else:
                line.append('')
            line.append(row.date_begin)
            if previous_card:
                pval = int(previous_card.discount_value) if previous_card.discount_value else 0
                line.append('{val}%'.format(val=pval))
            else:
                line.append('')
            val = int(row.discount_value) if row.discount_value else 0
            self.discounts[val] += 1
            line.append('{val}%'.format(val=val))
            line.append(row.first_payment.date)
            rows.append(line)
        self.total = len(rows)
        return rows

    def write_data(self):
        for row in self.get_data():
            row_step = 0
            red = False
            if row[4] and row[5]:
                if (row[5] - row[4]).days > 1:
                    red = True
            for i, cell in enumerate(row):
                if red:
                    style = self.red_font
                else:
                    style = self.table_styles.get(i, styles.style)
                if cell and i in [4, 5, 8]:
                    cell = cell.strftime('%d.%m.%Y')
                self.ws.write(self.row_num, i, cell, style)
            self.row_num += (1 + row_step)

    def write_bottom(self):
        self.ws.write(self.row_num, 0, _('total'), styles.styleth)
        self.ws.write(self.row_num + 1, 0, self.total, styles.styleth)
        self.ws.write(self.row_num, 2, _('including:'), styles.styleth)
        for i, discount in enumerate(self.discounts):
            discount_h = '{val}%'.format(val=discount)
            col = 3 + i
            cnt = self.discounts.get(discount)
            self.ws.write(self.row_num, col, discount_h, styles.styleth)
            self.ws.write(self.row_num + 1, col, cnt, styles.styleth)
