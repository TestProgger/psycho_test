import secrets

from psycho_test import models
from subject import models as subject_models
from psycho_test.api.psycho_test import serializers
from utils.permissions import IsSubjectSet
from utils.mixins import ResponseMixin
from rest_framework.viewsets import ViewSet
from rest_framework.request import Request


class PsychoTestViewSet(ViewSet, ResponseMixin):
    permission_classes = [IsSubjectSet, ]

    def list(self, request: Request):
        serializer = serializers.ListPsychoTestModelSerializer(
            instance=models.PsychoTest.objects.filter(is_visible=True),
            many=True
        )

        return self.success_response(body={"list": serializer.data})

    def start_test(self, request: Request):
        serializer = serializers.StartPsychoTestSerializer(data=request.data)

        if not serializer.is_valid():
            return self.error_response(message=serializer.errors)

        try:
            psycho_test = models.PsychoTest.objects.get(id=serializer.validated_data['id'])
            subject_test = subject_models.SubjectToPsychoTest.objects.filter(
                psycho_test=psycho_test,
                subject=request.subject,
                is_completed=False
            ).first()

            if not subject_test:
                subject_test = subject_models.SubjectToPsychoTest.objects.create(
                    psycho_test=psycho_test,
                    subject=request.subject,
                    token=secrets.token_urlsafe(64)
                )

        except Exception as ex:
            return self.error_response(message=ex.__str__())

        return self.success_response(body={"subject_test_id": subject_test.id, 'token': subject_test.token})

    def end_test(self, request: Request):
        serializer = serializers.EndPsychoTestSerializer(data=request.data)

        if not serializer.is_valid():
            return self.error_response(message=serializer.errors)

        try:
            subject_test = subject_models.SubjectToPsychoTest.objects.get(
                id=serializer.validated_data['id'],
                subject=request.subject
            )

            if subject_test.is_completed:
                return self.success_response()

            subject_test.is_completed = True
            subject_test.save()
        except Exception as ex:
            return self.error_response(message=ex.__str__())

        return self.success_response()

