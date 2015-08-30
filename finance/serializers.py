from datetime import date

from rest_framework import serializers

from .models import Credit, Payment
from .forms import FormCredit


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
        data['count'] = 1
        for credit in self.context['request'].data['credits']:
            data['amount'] = credit['amount']
            data['schedule'] = credit['date']
            form = FormCredit(data)
            if form.is_valid():
                form.save()
            else:
                print form.errors
        return payment
