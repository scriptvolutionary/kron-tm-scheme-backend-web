from rest_framework import serializers

from django.contrib.auth.models import *
from .models import *


class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ['url', 'username', 'password', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Group
        fields = ['url', 'name']


class FacilitySerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Facility
        fields = '__all__'


class ScriptSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Script
        fields = '__all__'


class PropertySerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Property
        fields = '__all__'


class FormSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Form
        fields = '__all__'


class FacilityTypeSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = FacilityType
        fields = '__all__'


class EventSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Event
        fields = '__all__'


class FormScriptSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = FormScript
        fields = '__all__'