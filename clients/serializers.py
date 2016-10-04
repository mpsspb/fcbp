from datetime import date, timedelta, datetime
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


class GuestClubCardSerializer(serializers.ModelSerializer):

    class Meta:
        model = GuestClubCard


class FreezeClubCardSerializer(serializers.ModelSerializer):
    tdate = serializers.DateTimeField(read_only=True)

    class Meta:
        model = FreezeClubCard


class FitnessClubCardSerializer(serializers.ModelSerializer):
    employee = serializers.CharField(read_only=True)

    class Meta:
        model = FitnessClubCard


class PersonalClubCardSerializer(serializers.ModelSerializer):
    employee = serializers.CharField(read_only=True)

    class Meta:
        model = PersonalClubCard


class ProlongationClubCardSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProlongationClubCard


class ActiveListSerializer(serializers.ListSerializer):

    """
    Exclude archive/disabled objects.
    """

    def to_representation(self, data):
        data = data.exclude(status=0)
        return super(ActiveListSerializer, self).to_representation(data)


class ArchiveListSerializer(serializers.ListSerializer):

    """
    Archive/disabled objects.
    """

    def to_representation(self, data):
        data = data.filter(status=False)
        return super(ArchiveListSerializer, self).to_representation(data)


class ClientClubCardSerializer(serializers.ModelSerializer):

    useclientclubcard_set = UseClientClubCardSerializer(many=True,
                                                        read_only=True)
    guestclubcard_set = GuestClubCardSerializer(many=True, read_only=True)
    client_name = serializers.CharField(read_only=True)
    discount_description = serializers.CharField(read_only=True)
    client_mobile = serializers.IntegerField(read_only=True)
    client_uid = serializers.IntegerField(read_only=True)
    client_card = serializers.IntegerField(read_only=True)
    personalclubcard_set = PersonalClubCardSerializer(many=True,
                                                      read_only=True)
    fitnessclubcard_set = FitnessClubCardSerializer(many=True,
                                                    read_only=True)
    freezeclubcard_set = FreezeClubCardSerializer(many=True, read_only=True)
    prolongationclubcard_set = ProlongationClubCardSerializer(many=True,
                                                              read_only=True)
    credit_set = CreditSerializer(many=True, read_only=True)
    payment_set = PaymentSerializer(many=True, read_only=True)

    class Meta:
        list_serializer_class = ActiveListSerializer
        model = ClientClubCard
        fields = ('id', 'club_card', 'status', 'date', 'date_start',
                  'date_begin', 'date_end', 'name', 'client', 'is_online',
                  'rest_days', 'rest_visits', 'useclientclubcard_set',
                  'rest_guest', 'guest_training', 'guestclubcard_set',
                  'fitness_testing_discount', 'personal_training',
                  'personalclubcard_set', 'fitnessclubcard_set',
                  'rest_freeze', 'rest_freeze_times', 'is_frozen',
                  'freezeclubcard_set', 'prolongationclubcard_set',
                  'client_name', 'credit_set', 'payment_set', 'client_card',
                  'client_mobile', 'is_paid_activate', 'paid_activate_amount',
                  'discount_amount', 'bonus_amount', 'client_uid',
                  'block_comment', 'employee', 'discount_description')
        read_only_fields = ('id', )

    def create(self, validated_data,):
        data = self.context['request'].data.copy()
        data['count'] = 1
        data['status'] = 2
        data['date_start'] = date.today()
        fclub_card = FormClientClubCard(data)
        if fclub_card.is_valid():
            club_card = fclub_card.save()
            data['club_card'] = club_card.pk
            finance(data)
        else:
            print fclub_card.errors
        return club_card


class FreezeAquaSerializer(serializers.ModelSerializer):
    tdate = serializers.DateTimeField(read_only=True)

    class Meta:
        model = FreezeAqua


class ProlongationAquaSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProlongationAqua


class ClientExtraSerializer(serializers.ModelSerializer):

    """
    Serializer for saving or update data for multi-client's products.
    """
    class Meta:
        model = Client
        fields = (
            'id', 'first_name', 'last_name', 'patronymic', 'born', 'uid',
            'mobile', 'card', 'initials')
        read_only_fields = ('id', 'uid', 'mobile', 'card', 'initials')


class ClientAquaAerobicsSerializer(serializers.ModelSerializer):
    useclientaquaaerobics_set = UseClientAquaAerobicsSerializer(many=True,
                                                                read_only=True)
    rest_visits = serializers.IntegerField(read_only=True)
    is_online = serializers.IntegerField(read_only=True)
    is_frozen = serializers.BooleanField(read_only=True)
    name = serializers.CharField(read_only=True)
    client_name = serializers.CharField(read_only=True)
    rest_days = serializers.IntegerField(read_only=True)
    client_uid = serializers.IntegerField(read_only=True)
    client_card = serializers.IntegerField(read_only=True)
    client_mobile = serializers.IntegerField(read_only=True)
    credit_set = CreditSerializer(many=True, read_only=True)
    payment_set = PaymentSerializer(many=True, read_only=True)
    freezeaqua_set = FreezeAquaSerializer(many=True, read_only=True)
    prolongationaqua_set = ProlongationAquaSerializer(
        many=True, read_only=True)

    extra_client = ClientExtraSerializer(many=True, read_only=True)

    class Meta:
        list_serializer_class = ActiveListSerializer
        model = ClientAquaAerobics

    def create(self, validated_data,):
        data = self.context['request'].data.copy()
        data['count'] = 1
        data['status'] = 2
        data['date_start'] = date.today()
        faqua_aerobics = FormClientAquaAerobics(data)
        if faqua_aerobics.is_valid():
            aqua_aerobics = faqua_aerobics.save()
            for ex in data['extraclients']:
                born = ex['born']
                born = datetime.strptime(ex['born'], '%Y-%m-%d').date()
                ex['born'] = born
                cl = ClientExtraSerializer(data=ex)
                if cl.is_valid():
                    cl = Client.objects\
                               .get_or_create(first_name=ex['first_name'],
                                              last_name=ex['last_name'],
                                              patronymic=ex['patronymic'],
                                              born=born)[0]
                    ex_aqua = {}
                    ex_aqua['client'] = cl.pk
                    ex_aqua['client_aqua'] = aqua_aerobics.pk
                    faqua_aerobics = FormAquaAerobicsClients(ex_aqua)
                    if faqua_aerobics.is_valid():
                        faqua_aerobics.save()
                    else:
                        print 'aqua_ex: %s' % faqua_aerobics.errors
                else:
                    print 'client_ex: %s' % cl.errors
            data['aqua_aerobics'] = aqua_aerobics.pk
            finance(data)
        else:
            print faqua_aerobics.errors
        return aqua_aerobics


class ClientAquaAerobicsFullSerializer(serializers.ModelSerializer):
    useclientaquaaerobics_set = UseClientAquaAerobicsSerializer(many=True,
                                                                read_only=True)

    class Meta:
        list_serializer_class = ActiveListSerializer
        model = ClientAquaAerobicsFull
        fields = ('id', 'aqua_aerobics', 'status', 'date', 'date_start',
                  'date_begin', 'date_end', 'useclientaquaaerobics_set',
                  'rest_days', 'name', 'client', 'rest_visits', 'is_online',
                  'is_frozen')


class FreezeTicketSerializer(serializers.ModelSerializer):
    tdate = serializers.DateTimeField(read_only=True)

    class Meta:
        model = FreezeTicket


class ProlongationTicketSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProlongationTicket


class ClientTicketSerializer(serializers.ModelSerializer):
    useclientticket_set = UseClientTicketSerializer(many=True,
                                                    read_only=True)
    client_name = serializers.CharField(read_only=True)
    client_mobile = serializers.IntegerField(read_only=True)
    client_uid = serializers.IntegerField(read_only=True)
    client_card = serializers.IntegerField(read_only=True)
    is_frozen = serializers.BooleanField(read_only=True)
    is_online = serializers.IntegerField(read_only=True)
    rest_visits = serializers.IntegerField(read_only=True)
    credit_set = CreditSerializer(many=True, read_only=True)
    payment_set = PaymentSerializer(many=True, read_only=True)
    name = serializers.CharField(read_only=True)
    freezeticket_set = FreezeTicketSerializer(many=True, read_only=True)
    prolongationticket_set = ProlongationTicketSerializer(
        many=True, read_only=True)

    class Meta:
        list_serializer_class = ActiveListSerializer
        model = ClientTicket

    def create(self, validated_data,):
        data = self.context['request'].data.copy()
        data['count'] = 1
        data['status'] = 2
        data['date_start'] = date.today()
        obj = Ticket.objects.get(pk=data['ticket'])
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
    client_name = serializers.CharField(read_only=True)

    class Meta:
        model = ClientPersonal
        fields = ('id', 'personal', 'status', 'date', 'date_start',
                  'date_begin', 'date_end', 'name', 'client', 'is_online',
                  'rest_days', 'rest_visits', 'useclientpersonal_set',
                  'client_name')

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
    client_name = serializers.CharField(read_only=True)

    class Meta:
        model = ClientTiming
        fields = ('id', 'timing', 'status', 'date', 'date_start', 'client',
                  'date_begin', 'date_end', 'name', 'useclienttiming_set',
                  'rest_days', 'rest_minutes', 'client_name')

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


class ClientOnlineSerializer(serializers.ModelSerializer):

    class Meta:
        model = ClientOnline


class ClientSerializer(serializers.ModelSerializer):
    avatar = Base64ImageField(
        max_length=None, use_url=True
    )
    clientclubcard_set = ClientClubCardSerializer(
        many=True, read_only=True)
    clientaquaaerobicsfull_set = ClientAquaAerobicsFullSerializer(
        many=True,
        read_only=True)
    clientticket_set = ClientTicketSerializer(many=True, read_only=True)
    clientpersonal_set = ClientPersonalSerializer(many=True, read_only=True)
    clienttiming_set = ClientTimingSerializer(many=True, read_only=True)

    credit_set = CreditSerializer(many=True, read_only=True)
    debt_set = DebtSerializer(many=True, read_only=True)
    debtupcoming_set = DebtUpcomingSerializer(many=True, read_only=True)

    online_clubcard = serializers.BooleanField(read_only=True)
    online_aqua = serializers.BooleanField(read_only=True)
    online_ticket = serializers.BooleanField(read_only=True)
    online_personal = serializers.BooleanField(read_only=True)
    introductory_employee_name = serializers.CharField(read_only=True)
    avatar_url = serializers.CharField(read_only=True)
    full_name = serializers.CharField(read_only=True)
    passport = serializers.CharField(read_only=True)
    clientonline_set = ClientOnlineSerializer(many=True, read_only=True)

    class Meta:
        model = Client
        read_only_fields = ('id', 'full_name', 'avatar_url', 'date',
                            'clientonline_set')


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
