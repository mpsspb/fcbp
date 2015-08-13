from rest_framework import serializers

from .models import Period, ClubCard, AquaAerobics


class PeriodSerializer(serializers.ModelSerializer):

    class Meta:
        model = Period

        fields = ('id', 'value', 'is_active', 'is_month' )
        read_only_fields = ('id', )


class ClubCardSerializer(serializers.ModelSerializer):
    period_data = PeriodSerializer(read_only=True)

    class Meta:
        model = ClubCard

        fields = ('name', 'max_visit', 'period', 'period_data',
                  'is_full_time', 'is_active',
                  'period_freeze', 'period_activation',
                  'period_prolongation', 'clients_count', 
                  'guest_training', 'fitness_testing_discount',
                  'personal_training', 'price')
        read_only_fields = ('id', 'period_data',)


class AquaAerobicsSerializer(serializers.ModelSerializer):
    period_data = PeriodSerializer(read_only=True)

    class Meta:
        model = AquaAerobics

        fields = ('name', 'max_visit', 'period', 'period_data',
                  'is_full_time', 'is_active',
                  'period_prolongation', 'clients_count', 
                  'price')
        read_only_fields = ('id', 'period_data',)
