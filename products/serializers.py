from rest_framework import serializers

from .models import Period, ClubCard


class PeriodSerializer(serializers.ModelSerializer):

    class Meta:
        model = Period

        fields = ('id', 'value', 'is_active', )
        read_only_fields = ('id', )


class ClubCardSerializer(serializers.ModelSerializer):

    class Meta:
        model = ClubCard

        fields = ('name', 'max_visit', 'period',
                  'is_full_time', 'is_active',
                  'period_freeze', 'period_activation',
                  'guest_training', 'fitness_testing_discount',
                  'personal_training', 'price')
        read_only_fields = ('id', )
