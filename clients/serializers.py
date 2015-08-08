from rest_framework import serializers

from .models import Client


class ClientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Client

        fields = ('id', 'first_name', 'last_name', 'patronymic',
                  'born',  'gender', 'mobile', 'address', 'passport',
                  'phone', 'email', 'avatar')
        read_only_fields = ('id', )
