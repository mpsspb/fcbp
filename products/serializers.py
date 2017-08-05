# -*- coding: utf-8 -*-
from rest_framework import serializers

from employees.models import Position
from .models import (Period, ClubCard, AquaAerobics, Sport, Ticket,
                     Personal, PersonalPosition, Timing, Discount,
                     Training, CardText, CardTextItems)


class DiscountSerializer(serializers.ModelSerializer):

    class Meta:
        model = Discount


class PeriodSerializer(serializers.ModelSerializer):

    class Meta:
        model = Period
        fields = ('id', 'value', 'is_active', 'is_month')
        read_only_fields = ('id', )


class ClubCardSerializer(serializers.ModelSerializer):
    period_data = PeriodSerializer(read_only=True)

    class Meta:
        model = ClubCard
        read_only_fields = ('id', 'period_data',)


class AquaAerobicsSerializer(serializers.ModelSerializer):
    period_data = PeriodSerializer(read_only=True)

    class Meta:
        model = AquaAerobics
        read_only_fields = ('id', 'period_data',)


class SportSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sport


class TrainingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Training


class TicketSerializer(serializers.ModelSerializer):
    period_data = PeriodSerializer(read_only=True)
    sport_data = SportSerializer(read_only=True)

    class Meta:
        model = Ticket

        fields = ('id', 'name', 'max_visit', 'period', 'period_data',
                  'sport', 'sport_data', 'sport_name',
                  'is_full_time', 'is_active',
                  'period_prolongation', 'price')
        read_only_fields = ('id', 'period_data', 'sport_data', 'sport_name')


class PositionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Position


class PersonalPositionSerializer(serializers.ModelSerializer):
    position = PositionSerializer()

    class Meta:
        model = PersonalPosition
        fields = ('position', )


class PersonalSerializer(serializers.ModelSerializer):
    period_data = PeriodSerializer(read_only=True)
    positions = PersonalPositionSerializer(many=True, read_only=True)
    positions_pks = serializers.ListField(
        read_only=True, allow_null=True)

    class Meta:
        model = Personal
        read_only = ('id', 'period_data', 'positions', 'positions_pks')

    def create(self, validated_data, ):
        positions = self.context['request'].data['positions']
        positions = Position.objects.filter(pk__in=positions)
        personal = Personal.objects.create(**validated_data)
        for position in positions:
            PersonalPosition.objects.create(personal=personal,
                                            position=position)
        return personal

    def update(self, instance, validated_data, ):
        positions = self.context['request'].data['positions_pks']
        new_p = [p for p in positions if p not in instance.positions_pks]
        del_p = [p for p in instance.positions_pks if p not in positions]
        instance = super(PersonalSerializer, self).update(
            instance, validated_data)
        for position in new_p:
            PersonalPosition.objects.create(
                personal=instance, position_id=position)
        for position in del_p:
            PersonalPosition.objects.get(
                personal=instance, position_id=position).delete()
        return instance


class TimingSerializer(serializers.ModelSerializer):
    period_data = PeriodSerializer(read_only=True)

    class Meta:
        model = Timing

        fields = ('id', 'name', 'period', 'period_data',
                  'is_active', 'minutes', 'period_freeze',
                  'period_prolongation', 'clients_count',
                  'price')
        read_only_fields = ('id', 'period_data',)


class CardTextItemsSerializer(serializers.ModelSerializer):

    class Meta:
        model = CardTextItems
        read_only_fields = ('id',)


class CardTextSerializer(serializers.ModelSerializer):
    cardtextitems_set = CardTextItemsSerializer(many=True, read_only=True)
    name = serializers.CharField(read_only=True)

    class Meta:
        model = CardText
        read_only_fields = ('id',)
