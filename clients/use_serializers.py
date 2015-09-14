from rest_framework import serializers

from .models import UseClientClubCard, UseClientAquaAerobics
from .models import UseClientTicket, UseClientPersonal, UseClientTiming


class UseClientClubCardSerializer(serializers.ModelSerializer):

    class Meta:
        model = UseClientClubCard


class UseClientAquaAerobicsSerializer(serializers.ModelSerializer):

    class Meta:
        model = UseClientAquaAerobics


class UseClientTicketSerializer(serializers.ModelSerializer):

    class Meta:
        model = UseClientTicket


class UseClientPersonalSerializer(serializers.ModelSerializer):

    class Meta:
        model = UseClientPersonal


class UseClientTimingSerializer(serializers.ModelSerializer):

    class Meta:
        model = UseClientTiming
