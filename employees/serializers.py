from rest_framework import serializers

from .models import *


class PositionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Position
        fields = ('id', 'name', 'is_active', )
        read_only_fields = ('id', )


class EmployeeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Employee
        fields = ('id', 'first_name', 'last_name', 'patronymic',
                  'full_name', 'born', 'initials', 'is_seller')
        read_only_fields = ('id', )
