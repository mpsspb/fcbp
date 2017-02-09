# -*- coding: utf-8 -*-
import uuid
from datetime import datetime, date, timedelta

from django.db.models.loading import get_model


class WritePayment(object):

    def add_payment(self, payment_type, force=False):
        payment_model = get_model('finance', 'Payment')
        if (not self.pk or force) and self.is_paid:
            if hasattr(self, 'parent'):
                client = self.parent.client
                goods = self.parent
            else:
                client = self.client
                goods = self
            p_data = {
                'date': datetime.now(),
                'payment_type': payment_type,
                'amount': self.amount,
                'count': 1,
                'extra_uid': uuid.uuid4(),
                'extra_text': self.paid_text,
                'client': client,
                self.payment_goods: goods
            }
            payment_model.objects.create(**p_data)


class Prolongation(object):

    def parent_upd(self, *args, **kwargs):
        days = self.days
        parent = self.parent
        is_delete = kwargs.get('is_delete')
        if is_delete:
            parent.date_end = parent.date_end - timedelta(days)
        else:
            parent.date_end = parent.date_end + timedelta(days)
        parent.save()


class Property(object):

    """ Generic property need for all services """
    @property
    def client_mobile(self):
        return self.client.mobile

    @property
    def client_uid(self):
        return self.client.uid

    @property
    def client_name(self):
        return self.client.full_name

    @property
    def client_card(self):
        return self.client.card

    def escape_frozen(self):
        freeze_model = get_model('clients', self.freeze_class)
        filtr = {freeze_model.product: self, 'fdate__lte': date.today()}
        freezes = freeze_model.objects.filter(**filtr)
        for f in freezes:
            if f.tdate >= date.today():
                days_freeze = (date.today() - f.fdate).days
                days_back = (f.tdate - date.today()).days + 1
                self.date_end = self.date_end - timedelta(days_back)
                self.save()
                f.days = days_freeze
                f.save()

    @property
    def name(self):
        return self.product.name

    def full_name(self):
        return self.product.full_name

    def first_visit(self):
        return self.visits.all().order_by('date').first()

    def is_full_time(self):
        return self.product.is_full_time

    def similar_products(self):
        model = self.product._meta.model
        period = self.product.period
        products = model.objects.filter(is_active=True, period=period)
        return products.exclude(pk=self.product.pk)

    def price(self):
        return self.product.price
