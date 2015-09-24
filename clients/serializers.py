from datetime import date, timedelta
from dateutil.relativedelta import relativedelta

from rest_framework import serializers

from .models import *
from .forms import *
from .use_serializers import *
from products.models import *
from finance.serializers import *
from finance.forms import *


class Base64ImageField(serializers.ImageField):
    """
    A Django REST framework field for handling image-uploads through
    raw post data.
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
            # 12 characters are more than enough.
            file_name = str(uuid.uuid4())[:12]
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
        read_only_fields = ('id', )

    def create(self, validated_data,):
        data = self.context['request'].data.copy()
        data['count'] = 1
        data['status'] = 2
        data['date_start'] = date.today()
        data['date_begin'] = date.today()
        obj = ClubCard.objects.get(pk=data['club_card'])
        data['date_end'] = date_end(data['date_begin'], obj)
        fclub_card = FormClientClubCard(data)
        if fclub_card.is_valid():
            club_card = fclub_card.save()
            data['club_card'] = club_card.pk
            finance(data)
        else:
            print fclub_card.errors
        return club_card


class ClientAquaAerobicsSerializer(serializers.ModelSerializer):
    useclientaquaaerobics_set = UseClientAquaAerobicsSerializer(many=True,
                                                                read_only=True)

    class Meta:
        model = ClientAquaAerobics
        fields = ('id', 'aqua_aerobics', 'status', 'date', 'date_start',
                  'date_begin', 'date_end', 'useclientaquaaerobics_set',
                  'rest_days', 'name', 'client', 'rest_visits')

    def create(self, validated_data,):
        data = self.context['request'].data.copy()
        data['count'] = 1
        data['status'] = 2
        data['date_start'] = date.today()
        data['date_begin'] = date.today()
        obj = AquaAerobics.objects.get(pk=data['aqua_aerobics'])
        data['date_end'] = date_end(data['date_begin'], obj)
        faqua_aerobics = FormClientAquaAerobics(data)
        if faqua_aerobics.is_valid():
            aqua_aerobics = faqua_aerobics.save()
            data['aqua_aerobics'] = aqua_aerobics.pk
            finance(data)
        else:
            print faqua_aerobics.errors
        return aqua_aerobics


class ClientTicketSerializer(serializers.ModelSerializer):
    useclientticket_set = UseClientTicketSerializer(many=True,
                                                    read_only=True)

    class Meta:
        model = ClientTicket
        fields = ('id', 'ticket', 'status', 'date', 'date_start',
                  'date_begin', 'date_end', 'name', 'useclientticket_set',
                  'rest_days', 'rest_visits', 'client')

    def create(self, validated_data,):
        data = self.context['request'].data.copy()
        data['count'] = 1
        data['status'] = 2
        data['date_start'] = date.today()
        data['date_begin'] = date.today()
        obj = Ticket.objects.get(pk=data['ticket'])
        data['date_end'] = date_end(data['date_begin'], obj)
        fticket = FormClientTicket(data)
        if fticket.is_valid():
            ticket = fticket.save()
            data['ticket'] = ticket.pk
            finance(data)
        else:
            print fticket.errors
        return ticket


class ClientPersonalSerializer(serializers.ModelSerializer):
    useclientpersonal_set = UseClientPersonalSerializer(many=True,
                                                        read_only=True)

    class Meta:
        model = ClientPersonal
        fields = ('id', 'personal', 'status', 'date', 'date_start',
                  'date_begin', 'date_end', 'name', 'client',
                  'rest_days', 'rest_visits', 'useclientpersonal_set')

    def create(self, validated_data,):
        data = self.context['request'].data.copy()
        data['count'] = 1
        data['status'] = 2
        data['date_start'] = date.today()
        data['date_begin'] = date.today()
        obj = Personal.objects.get(pk=data['personal'])
        data['date_end'] = date_end(data['date_begin'], obj)
        fpersonal = FormClientPersonal(data)
        if fpersonal.is_valid():
            personal = fpersonal.save()
            data['personal'] = personal.pk
            finance(data)
        else:
            print fpersonal.errors
        return personal


class ClientTimingSerializer(serializers.ModelSerializer):
    useclienttiming_set = UseClientTimingSerializer(many=True, read_only=True)

    class Meta:
        model = ClientTiming
        fields = ('id', 'timing', 'status', 'date', 'date_start', 'client',
                  'date_begin', 'date_end', 'name', 'useclienttiming_set',
                  'rest_days', 'rest_minutes')

    def create(self, validated_data,):
        data = self.context['request'].data.copy()
        data['count'] = 1
        data['status'] = 2
        data['date_start'] = date.today()
        data['date_begin'] = date.today()
        obj = Timing.objects.get(pk=data['timing'])
        data['date_end'] = date_end(data['date_begin'], obj)
        ftiming = FormClientTiming(data)
        if ftiming.is_valid():
            timing = ftiming.save()
            data['timing'] = timing.pk
            finance(data)
        else:
            print ftiming.errors
        return timing


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

    credit_set = CreditSerializer(many=True, read_only=True)
    debt_set = DebtSerializer(many=True, read_only=True)
    debtupcoming_set = DebtUpcomingSerializer(many=True, read_only=True)

    class Meta:
        model = Client
        fields = ('id', 'first_name', 'last_name', 'patronymic',
                  'born',  'gender', 'mobile', 'address', 'passport',
                  'phone', 'email', 'avatar', 'date', 'clientclubcard_set',
                  'avatar_url', 'full_name', 'uid', 'clientaquaaerobics_set',
                  'clientticket_set', 'clientpersonal_set', 'clienttiming_set',
                  'credit_set', 'debt_set', 'debtupcoming_set',
                  'introductory_date', 'introductory_employee',
                  )
        read_only_fields = ('id', 'full_name', 'avatar_url', 'uid',
                            'date')


def finance(data):
    """
    Finance records for the service of the client.
    """
    # Add Payment
    fpayment = FormPayment(data)
    if fpayment.is_valid():
        fpayment.save()
    else:
        print fpayment.errors
    # Create credit schedule
    for credit in data['credits']:
        data['amount'] = credit['amount']
        data['schedule'] = credit['date']
        form = FormCredit(data)
        if form.is_valid():
            form.save()
        else:
            print form.errors


def date_end(date_begin, obj):
    """
    Return date end for the obj
    """
    if obj.period.is_month:
        months = obj.period.value
        return date_begin + relativedelta(months=months)
    else:
        days = obj.period.value
        return date_begin + timedelta(days=days)
