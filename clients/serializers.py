from rest_framework import serializers

from .models import Client, ClientClubCard, ClientAquaAerobics, ClientTicket
from .models import ClientPersonal, ClientTiming
from .use_serializers import *


class Base64ImageField(serializers.ImageField):
    """
    A Django REST framework field for handling image-uploads through raw post data.
    It uses base64 for encoding and decoding the contents of the file.

    Heavily based on
    https://github.com/tomchristie/django-rest-framework/pull/1268
    """

    def to_internal_value(self, data):
        from django.core.files.base import ContentFile
        import base64
        import uuid

        # Check if this is a base64 string
        if isinstance(data, basestring):
            # Check if the base64 string is in the "data:" format
            if 'data:' in data and ';base64,' in data:
                # Break out the header from the base64 content
                header, data = data.split(';base64,')

            # Try to decode the file. Return validation error if it fails.
            try:
                decoded_file = base64.b64decode(data)
            except TypeError:
                self.fail('invalid_image')

            # Generate file name:
            file_name = str(uuid.uuid4())[:12] # 12 characters are more than enough.
            # Get the file name extension:
            file_extension = self.get_file_extension(file_name, decoded_file)

            complete_file_name = "%s.%s" % (file_name, file_extension, )

            data = ContentFile(decoded_file, name=complete_file_name)

        return super(Base64ImageField, self).to_internal_value(data)

    def get_file_extension(self, file_name, decoded_file):
        import imghdr

        extension = imghdr.what(file_name, decoded_file)
        extension = "jpg" if extension == "jpeg" else extension

        return extension


class ClientClubCardSerializer(serializers.ModelSerializer):
    useclientclubcard_set = UseClientClubCardSerializer(many=True,
                                                        read_only=True)

    class Meta:
        model = ClientClubCard

        fields = ('id', 'club_card', 'status', 'date', 'date_start',
                  'date_begin', 'date_end', 'name', 'client',
                  'rest_days', 'rest_visits', 'useclientclubcard_set')


class ClientAquaAerobicsSerializer(serializers.ModelSerializer):
    useclientaquaaerobics_set = UseClientAquaAerobicsSerializer(many=True,
                                                                read_only=True)

    class Meta:
        model = ClientAquaAerobics

        fields = ('id', 'aqua_aerobics', 'status', 'date', 'date_start',
                  'date_begin', 'date_end', 'useclientaquaaerobics_set',
                  'rest_days', 'name', 'client', 'rest_visits')


class ClientTicketSerializer(serializers.ModelSerializer):

    class Meta:
        model = ClientTicket

        fields = ('id', 'ticket', 'status', 'date', 'date_start',
                  'date_begin', 'date_end', 'name',
                  'rest_days', 'rest_visits')


class ClientPersonalSerializer(serializers.ModelSerializer):

    class Meta:
        model = ClientPersonal

        fields = ('id', 'personal', 'status', 'date', 'date_start',
                  'date_begin', 'date_end', 'name',
                  'rest_days', 'rest_visits')


class ClientTimingSerializer(serializers.ModelSerializer):
    useclienttiming_set = UseClientTimingSerializer(many=True, read_only=True)

    class Meta:
        model = ClientTiming

        fields = ('id', 'timing', 'status', 'date', 'date_start', 'client',
                  'date_begin', 'date_end', 'name', 'useclienttiming_set',
                  'rest_days', 'rest_minutes')


class ClientSerializer(serializers.ModelSerializer):
    avatar = Base64ImageField(
        max_length=None, use_url=True,
    )
    clientclubcard_set = ClientClubCardSerializer(many=True, read_only=True)
    clientaquaaerobics_set = ClientAquaAerobicsSerializer(many=True,
                                                          read_only=True)
    clientticket_set = ClientTicketSerializer(many=True, read_only=True)
    clientpersonal_set = ClientPersonalSerializer(many=True, read_only=True)
    clienttiming_set = ClientTimingSerializer(many=True, read_only=True)

    class Meta:
        model = Client

        fields = ('id', 'first_name', 'last_name', 'patronymic',
                  'born',  'gender', 'mobile', 'address', 'passport',
                  'phone', 'email', 'avatar', 'date', 'clientclubcard_set',
                  'avatar_url', 'full_name', 'uid', 'clientaquaaerobics_set',
                  'clientticket_set', 'clientpersonal_set', 'clienttiming_set'
                  )
        read_only_fields = ('id', 'full_name', 'avatar_url', 'uid',
                            'date')
