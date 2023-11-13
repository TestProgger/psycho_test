from datetime import timedelta

from django.utils import timezone
from rest_framework.viewsets import ViewSet
from rest_framework.permissions import AllowAny
from rest_framework.request import Request
from rest_framework.response import Response
from subject.api import serializers
from subject import models
import secrets
from utils.mixins import ResponseMixin
from django.conf import settings
import logging
from utils.decorators import log_viewset_action
logger = logging.getLogger('api')


class SubjectViewSet(ViewSet, ResponseMixin):
    permission_classes = (AllowAny, )

    @log_viewset_action(logger)
    def create_subject(self, request: Request):
        cookie = request.META.get("HTTP_COOKIE", '')
        if cookie:
            return self.success_response()

        serializer = serializers.CreateSubjectSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        subject = models.Subject.objects.create(
            **serializer.validated_data
        )

        subject_secret = secrets.token_urlsafe(60)
        subject_token = secrets.token_urlsafe(60)

        subject_identity = models.SubjectIdentity.objects.create(
            secret=subject_secret,
            token=subject_token,
            subject=subject,
            expires=timezone.now() + timedelta(settings.COOKIE_EXPIRATION_HOURS)
        )

        response = self.success_response(
            body={
                "id": subject.id,
                "secret": subject_secret,
                **serializer.validated_data
            }
        )
        response.set_cookie(
            key='Token', value=subject_token, httponly=True, max_age=timedelta(hours=settings.COOKIE_EXPIRATION_HOURS)
        )

        return response

    @log_viewset_action(logger)
    def renew_cookie(self, request: Request):
        return Response(
            # data={"cookie": request.META.get("HTTP_COOKIE")}
            data={}
        )

    @log_viewset_action(logger)
    def list_groups(self, request: Request):
        serializer = serializers.ListGroupsModelSerializer(
            instance=models.SubjectGroup.objects.all(),
            many=True
        )

        return self.success_response(body={'list': serializer.data})
