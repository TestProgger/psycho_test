import secrets

from psycho_test import models
from subject import models as subject_models
from psycho_test.api.psycho_test import serializers
from utils.permissions import IsSubjectSet
from utils.mixins import ResponseMixin
from rest_framework.viewsets import ViewSet
from rest_framework.request import Request
from django.db.models import Q
import logging
from utils.decorators import log_viewset_action
logger = logging.getLogger('api')


class PsychoTestViewSet(ViewSet, ResponseMixin):
    permission_classes = [IsSubjectSet, ]

    @log_viewset_action(logger)
    def list(self, request: Request):
        serializer = serializers.ListPsychoTestModelSerializer(
            instance=models.PsychoTest.objects.filter(is_visible=True),
            many=True
        )

        return self.success_response(body={"list": serializer.data})

    @log_viewset_action(logger)
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

        return self.success_response(
            body={
                "subject_test_id": subject_test.id,
                'token': subject_test.token,
                "test_name": psycho_test.name
            })

    @log_viewset_action(logger)
    def end_test(self, request: Request):
        serializer = serializers.EndPsychoTestSerializer(data=request.data)

        if not serializer.is_valid():
            return self.error_response(message=serializer.errors)

        subject_test = subject_models.SubjectToPsychoTest.objects \
            .filter(
                id=serializer.validated_data['id'],
                subject=request.subject,
                is_completed=False
            ).first()

        if not subject_test:
            return self.error_response(message="Вы не начали тест")

        questions = models.PsychoTestToQuestion.objects \
            .select_related('question') \
            .filter(
                psycho_test_id=subject_test.psycho_test_id
            )

        answered_questions = subject_models.SubjectToPsychoTestAnswer.objects \
            .select_related('answer', 'answer__score') \
            .filter(
                subject_test__psycho_test_id=subject_test.psycho_test_id,
                subject_test__is_completed=False,
                subject_test__subject=request.subject
            )

        if questions.count() != answered_questions.count():
            return self.error_response(
                message="Вы не ответили на все вопросы"
            )

        try:

            result_sum = 0
            for aq in answered_questions:
                result_sum += aq.answer.score.value

            logger.error(f"result_sum={result_sum} test_id={subject_test.psycho_test_id}")

            test_result: models.PsychoTestToResult = models.PsychoTestToResult.objects \
                .select_related('result') \
                .filter(
                    Q(score_min__lte=result_sum) & Q(score_max__gte=result_sum),
                    Q(psycho_test_id=subject_test.psycho_test_id)
                ).first()

            subject_models.SubjectToPsychoTestResult.objects.create(
                subject=request.subject,
                result=test_result
            )

            subject_test.is_completed = True
            subject_test.save()

        except Exception as ex:
            return self.error_response(message=ex.__str__())

        return self.success_response(
            body={
                "id": test_result.result.id,
                "title": test_result.result.name,
                "code": test_result.result.code
            }
        )

