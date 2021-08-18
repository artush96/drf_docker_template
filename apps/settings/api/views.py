from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.settings.models import Notification
from apps.settings.api.serializers import GeneralSettingsSerializer, TermsSerializer, NotificationsSerializer
from apps.settings.models import GeneralSettings, Terms


class GeneralSettingsDetailView(APIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = GeneralSettingsSerializer

    def get(self, *args, **kwargs):
        return Response(self.serializer_class(self.get_queryset()).data)

    @staticmethod
    def get_queryset(*args, **kwargs):
        GeneralSettings.objects.get(company_id=kwargs.get('company_id'))


class GeneralSettingsUpdateView(APIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = GeneralSettingsSerializer

    def put(self, request, *args, **kwargs):
        data = self.serializer_class(request.data).data
        obj = GeneralSettings.objects.get(company_id=kwargs.get('company_id')).update(**data)
        return Response(self.serializer_class(obj).data)


class TermsDetailView(APIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = TermsSerializer

    def get(self, *args, **kwargs):
        return Response(self.serializer_class(self.get_queryset()).data)

    @staticmethod
    def get_queryset(*args, **kwargs):
        Terms.objects.get(company_id=kwargs.get('company_id'))


class TermsUpdateView(APIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = TermsSerializer

    def put(self, request, *args, **kwargs):
        data = self.serializer_class(request.data).data
        obj = Terms.objects.get(company_id=kwargs.get('company_id')).update(**data)
        return Response(self.serializer_class(obj).data)


class NotificationDetailView(APIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = NotificationsSerializer

    def get(self, *args, **kwargs):
        return Response(self.serializer_class(self.get_queryset()).data)

    @staticmethod
    def get_queryset(*args, **kwargs):
        Notification.objects.get(company_id=kwargs.get('company_id'))


class NotificationUpdateView(APIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = NotificationsSerializer

    def put(self, request, *args, **kwargs):
        data = self.serializer_class(request.data).data
        obj = Notification.objects.get(company_id=kwargs.get('company_id')).update(**data)
        return Response(self.serializer_class(obj).data)
