from rest_framework import serializers

from employees.models import Position
from .models import Period, ClubCard, AquaAerobics, Sport, Ticket
from .models import Personal, PersonalPosition

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


class SportSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sport

        fields = ('id', 'name', 'is_active', )
        read_only_fields = ('id', )


class TicketSerializer(serializers.ModelSerializer):
    period_data = PeriodSerializer(read_only=True)
    sport_data = SportSerializer(read_only=True)

    class Meta:
        model = Ticket

        fields = ('name', 'max_visit', 'period', 'period_data',
                  'sport', 'sport_data', 'sport_name',
                  'is_full_time', 'is_active',
                  'period_prolongation', 'price')
        read_only_fields = ('id', 'period_data', 'sport_data', 'sport_name')


class PersonalPositionSerializer(serializers.ModelSerializer):

    class Meta:
        model = PersonalPosition


class PersonalSerializer(serializers.ModelSerializer):
    # positions = PersonalPositionSerializer(many=True)
    # positions = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    period_data = PeriodSerializer(read_only=True)

    class Meta:
        model = Personal
        fields = ('id', 'name', 'max_visit', 'period', 'period_data',
                  'clients_count', 'is_full_time', 'is_active',
                  'price', 'period_prolongation', 'positions', )
        read_only = ('id', 'period_data')

    def create (self, validated_data, ):
        positions = self.context['request'].data['positions']
        positions = Position.objects.filter(pk__in=positions)
        personal = Personal.objects.create(**validated_data)
        for position in positions:
            PersonalPosition.objects.create(personal=personal,
                                            position=position)
        return personal

