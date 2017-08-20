import uuid
from datetime import datetime

from rest_framework import serializers
from django.db.models.loading import get_model

from .models import OwnersClubCard, OwnersClientPersonal


class OwnersSerializer(object):

    def create(self, validated_data):
        data = self.context['request'].data.copy()
        classModel = self.Meta.model
        # Update product
        product_model = self.Meta.product_model
        product_name = self.Meta.product_name
        product = product_model.objects.get(pk=data.get(product_name))
        old_client = product.client
        product.client_id = data.get('client')
        product.save()
        # Added payment
        payment_model = get_model('finance', 'Payment')
        p_data = {
            'date': datetime.now(),
            'payment_type': data.get('payment_type'),
            'amount': data.get('amount'),
            'count': 1,
            'extra_uid': uuid.uuid4(),
            'extra_text': 'paid owner',
            'client': old_client,
            product_name: product
        }
        payment_model.objects.create(**p_data)
        validated_data.update({"client": old_client})
        return super(OwnersSerializer, self).create(validated_data)


class OwnersClubCardSerializer(OwnersSerializer, serializers.ModelSerializer):
    client_name = serializers.SerializerMethodField()

    def get_client_name(self, obj):
        return obj.client.initials

    class Meta:
        model = OwnersClubCard
        product_model = get_model('clients', 'ClientClubCard')
        product_name = 'club_card'


class OwnersPersonalSerializer(OwnersSerializer, serializers.ModelSerializer):
    client_name = serializers.SerializerMethodField()

    def get_client_name(self, obj):
        return obj.client.initials

    class Meta:
        model = OwnersClientPersonal
        product_model = get_model('clients', 'ClientPersonal')
        product_name = 'personal'
