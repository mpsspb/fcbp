from rest_framework import serializers

from .models import (UseClientClubCard, UseClientAquaAerobics,
                     UseClientTicket, UseClientPersonal, UseClientTiming,
                     ClubCardTrains)


class ClubCardTrainsSerializer(serializers.ModelSerializer):

    name = serializers.CharField(read_only=True)

    class Meta:
        model = ClubCardTrains


class UseClientClubCardSerializer(serializers.ModelSerializer):

    clubcardtrains_set = ClubCardTrainsSerializer(many=True, read_only=True)
    date = serializers.DateTimeField(required=False, allow_null=True)

    class Meta:
        model = UseClientClubCard


class UseClientAquaAerobicsSerializer(serializers.ModelSerializer):

    class Meta:
        model = UseClientAquaAerobics


class UseClientTicketSerializer(serializers.ModelSerializer):

    class Meta:
        model = UseClientTicket


class UseClientPersonalSerializer(serializers.ModelSerializer):
    instructor = serializers.ReadOnlyField(source='instructor.initials')

    class Meta:
        model = UseClientPersonal


class UseClientTimingSerializer(serializers.ModelSerializer):

    class Meta:
        model = UseClientTiming
