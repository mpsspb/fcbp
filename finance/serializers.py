from datetime import date, timedelta
from dateutil.relativedelta import relativedelta

from rest_framework import serializers

from .models import Credit, Payment
from .models_views import Debt, DebtUpcoming
from .forms import FormCredit, FormClientClubCard, FormClientAquaAerobics
from .forms import FormClientTicket, FormClientPersonal, FormClientTiming


class DebtSerializer(serializers.ModelSerializer):
    class Meta:
        model = Debt


class DebtUpcomingSerializer(serializers.ModelSerializer):
    class Meta:
        model = DebtUpcoming


class CreditSerializer(serializers.ModelSerializer):
    class Meta:
        model = Credit
        read_only_fields = ('id', )


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        read_only_fields = ('id', )

    def create(self, validated_data, ):
        payment = Payment.objects.create(**validated_data)
        data = self.context['request'].data.copy()
        # Create credit schedule
        data['count'] = 1
        for credit in self.context['request'].data['credits']:
            data['amount'] = credit['amount']
            data['schedule'] = credit['date']
            form = FormCredit(data)
            if form.is_valid():
                form.save()
            else:
                print form.errors
        # Create client product info
        data['status'] = 2
        data['date_start'] = date.today()
        data['date_begin'] = date.today()
        if payment.club_card:
            obj = payment.club_card
            data['date_end'] = date_end(data['date_begin'], obj)
            form = FormClientClubCard(data)
            if form.is_valid():
                form.save()
            else:
                print form.errors
        elif payment.aqua_aerobics:
            obj = payment.aqua_aerobics
            data['date_end'] = date_end(data['date_begin'], obj)
            form = FormClientAquaAerobics(data)
            if form.is_valid():
                form.save()
            else:
                print form.errors
        elif payment.ticket:
            obj = payment.ticket
            data['date_end'] = date_end(data['date_begin'], obj)
            form = FormClientTicket(data)
            if form.is_valid():
                form.save()
            else:
                print form.errors
        elif payment.personal:
            obj = payment.personal
            data['date_end'] = date_end(data['date_begin'], obj)
            form = FormClientPersonal(data)
            if form.is_valid():
                form.save()
            else:
                print form.errors
        elif payment.timing:
            obj = payment.timing
            data['date_end'] = date_end(data['date_begin'], obj)
            form = FormClientTiming(data)
            if form.is_valid():
                form.save()
            else:
                print form.errors

        return payment


def date_end(date_begin, obj):
    """
    Return date end for the obj
    """
    if obj.period.is_month:
        months = obj.period.value
        return date_begin + relativedelta(months=months)
    else:
        days = obj.period.value
        return date_begin + timedelta(days=days)
