from rest_framework import serializers

from .models import Period


class PeriodSerializer(serializers.ModelSerializer):

    class Meta:
        model = Period

        fields = ('id', 'value', 'is_active', )
        read_only_fields = ('id', )
