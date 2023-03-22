from rest_framework import viewsets
from rest_framework import permissions

from django.contrib.auth.models import *
from .models import *
from .serializers import *


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]


class FacilityViewSet(viewsets.ModelViewSet):
    queryset = Facility.objects.all()
    serializer_class = FacilitySerializer
    permission_classes = [permissions.IsAuthenticated]


class ScriptViewSet(viewsets.ModelViewSet):
    queryset = Script.objects.all()
    serializer_class = ScriptSerializer
    permission_classes = [permissions.IsAuthenticated]


class PropertyViewSet(viewsets.ModelViewSet):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
    permission_classes = [permissions.IsAuthenticated]


class FormViewSet(viewsets.ModelViewSet):
    queryset = Form.objects.all()
    serializer_class = FormSerializer
    permission_classes = [permissions.IsAuthenticated]


class FacilityTypeViewSet(viewsets.ModelViewSet):
    queryset = FacilityType.objects.all()
    serializer_class = FacilityTypeSerializer
    permission_classes = [permissions.IsAuthenticated]


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticated]


class FormScriptViewSet(viewsets.ModelViewSet):
    queryset = FormScript.objects.all()
    serializer_class = FormScriptSerializer
    permission_classes = [permissions.IsAuthenticated]