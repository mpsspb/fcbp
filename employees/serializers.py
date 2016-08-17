from rest_framework import serializers

from .models import *


class PositionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Position
        fields = ('id', 'name', 'is_active', )
        read_only_fields = ('id', )


class EmployeeSerializer(serializers.ModelSerializer):

    full_name = serializers.CharField(max_length=250)

    class Meta:
        model = Employee
        read_only_fields = ('id', 'full_name')
