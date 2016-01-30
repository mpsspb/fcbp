from rest_framework import serializers

from .models import ClientClubCard


class ClientClubCardSerial(serializers.ModelSerializer):
    """
    ClientClubCard light serializers only models fields.
    """
    name = serializers.CharField()
    discount_name = serializers.CharField()

    class Meta:
        model = ClientClubCard
