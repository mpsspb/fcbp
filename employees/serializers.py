from rest_framework import serializers

from .models import Position


class PositionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Position

        fields = ('id', 'name', 'is_active', )
        read_only_fields = ('id', )
