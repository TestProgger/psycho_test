from psycho_test import models
from subject import models as subject_models
from psycho_test.api.question import serializers
from utils.permissions import IsSubjectSet
from utils.mixins import ResponseMixin
from rest_framework.viewsets import ViewSet
from rest_framework.request import Request
import logging
from utils.decorators import log_viewset_action
logger = logging.getLogger('api')

class QuestionViewSet(ViewSet, ResponseMixin):
    permission_classes = [IsSubjectSet, ]

    @log_viewset_action(logger)
    def list(self, request: Request):
        serializer = serializers.ListQuestionSerializer(data=request.query_params)

        if not serializer.is_valid():
            return self.error_response(message=serializer.errors)

        response_body = []

        subject_test = subject_models.SubjectToPsychoTest.objects \
            .filter(
                id=serializer.validated_data['id'],
                subject=request.subject,
                is_completed=False
            ).first()

        if not subject_test:
            return self.error_response(message="Вы не начали тест")

        try:
            questions = models.PsychoTestToQuestion.objects \
                .select_related('question') \
                .filter(
                    psycho_test_id=subject_test.psycho_test_id
                )
            answered_count = 0
            all_count = 0
            for question in questions:
                question_body = {
                    'id': question.id,
                    'title': question.question.title,
                    'type': question.question.type.code,
                    'is_answered': False,
                    'answers': []
                }

                question_to_answers = models.PsychoTestQuestionToAnswer.objects \
                    .select_related('answer') \
                    .filter(
                        test_question_id=question.id
                    )

                for q_to_a in question_to_answers:
                    subject_q_to_a = subject_models.SubjectToPsychoTestAnswer.objects \
                        .filter(
                            subject_test__psycho_test_id=subject_test.psycho_test_id,
                            subject_test__is_completed=False,
                            subject_test__subject=request.subject,
                            answer_id=q_to_a.id
                        ).first()

                    if subject_q_to_a:
                        answered_count += 1
                        question_body['is_answered'] = True
                        question_body['answers'].append(
                            {
                                'id': q_to_a.id,
                                'title': q_to_a.answer.title,
                                'description': q_to_a.answer.description,
                                'is_checked': True
                            }
                        )
                    else:
                        question_body['answers'].append(
                            {
                                'id': q_to_a.id,
                                'title': q_to_a.answer.title,
                                'description': q_to_a.answer.description,
                                'is_checked': False
                            }
                        )
                response_body.append(question_body)
        except Exception as ex:
            return self.success_response(body={'list': []}, message=ex.__str__())

        return self.success_response(body={
            'list': response_body,
            "answered": answered_count,
            'total': questions.count()
        })
