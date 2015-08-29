from rest_framework import serializers

from .models import Credit, Payment


class CreditSerializer(serializers.ModelSerializer):

    class Meta:
        model = Credit
        read_only_fields = ('id', )


class PaymentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Payment
        read_only_fields = ('id', )
