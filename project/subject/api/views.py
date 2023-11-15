from datetime import timedelta

from django.http import HttpResponseRedirect
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
from utils.permissions import IsSubjectSet

logger = logging.getLogger('api')


class SubjectViewSet(ViewSet, ResponseMixin):
    permission_classes = (AllowAny, )

    @log_viewset_action(logger)
    def create_subject(self, request: Request):

        serializer = serializers.CreateSubjectSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        parent_subject = None
        subject_data = {**serializer.validated_data}
        if serializer.validated_data.get('secret'):
            parent_subject = models.Subject.objects.filter(
                subjectidentity__secret=serializer.validated_data.get('secret')
            ).first()

        if "secret" in subject_data:
            subject_data.pop("secret")

        subject = models.Subject.objects.create(
            **subject_data,
            parent=parent_subject
        )

        subject_secret = secrets.token_urlsafe(40)
        subject_token = secrets.token_urlsafe(40)

        subject_identity = models.SubjectIdentity.objects.create(
            secret=subject_secret,
            token=subject_token,
            subject=subject,
            expires=timezone.now() + timedelta(settings.COOKIE_EXPIRATION_HOURS)
        )

        response = self.success_response(
            body={
                "id": subject.id,
                "expires": int((timezone.now() + timedelta(hours=settings.COOKIE_EXPIRATION_HOURS)).timestamp()),
                **serializer.validated_data,
                "secret": subject_secret,
            }
        )
        response.set_cookie(
            key=settings.COOKIE_KEY, value=subject_token, httponly=True, max_age=timedelta(hours=settings.COOKIE_EXPIRATION_HOURS)
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


class LogoutSubjectViewSet(ViewSet, ResponseMixin):
    permission_classes = [IsSubjectSet]

    @log_viewset_action(logger)
    def logout(self, request: Request):
        response = self.success_response()
        response.delete_cookie(settings.COOKIE_KEY)
        return response
