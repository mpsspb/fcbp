from datetime import date

from rest_framework import serializers

from .models import *


class PositionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Position
        fields = ('id', 'name', 'is_active', )
        read_only_fields = ('id', )


class EmployeeSerializer(serializers.ModelSerializer):

    full_name = serializers.CharField(max_length=250, read_only=True)
    initials = serializers.CharField(max_length=250, read_only=True)
    position = serializers.CharField(read_only=True)

    class Meta:
        model = Employee
        read_only_fields = ('id', 'full_name')

    def update(self, instance, validated_data):
        instance = super(EmployeeSerializer, self).update(
            instance, validated_data)
        request = self.context.get('request')
        position = request.data.get('position')
        position_last = instance.positions.last()
        position_change = position_last and position_last.position != position
        if not position_last or position_change:
            today = date.today()
            EmployeePosition.objects.get_or_create(
                position_id=position, employee=instance, date_begin=today)
            if position_last:
                position_last.date_end = today
                position_last.save()
        return instance
