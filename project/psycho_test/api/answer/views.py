from psycho_test import models
from subject import models as subject_models
from psycho_test.api.answer import serializers
from utils.permissions import IsSubjectSet
from utils.mixins import ResponseMixin
from rest_framework.viewsets import ViewSet
from rest_framework.request import Request


class AnswerViewSet(ViewSet, ResponseMixin):
    permission_classes = (IsSubjectSet, )

    def set_answer(self, request: Request):
        serializer = serializers.SetAnswerSerializer(data=request.data)
        if not serializer.is_valid():
            return self.error_response(message=serializer.errors)

        try:
            test_question = models.PsychoTestToQuestion.objects.get(id=serializer.validated_data['question_id'])
            subject_test = subject_models.SubjectToPsychoTest.objects.get(
                is_completed=False,
                subject=request.subject,
                psycho_test_id=test_question.psycho_test_id
            )
        except:
            return self.error_response('Ошибка при сохранении ответа')

        if serializer.validated_data.get('answer_id'):
            try:
                new_answer = models.PsychoTestQuestionToAnswer.objects.get(
                    id=serializer.validated_data.get('answer_id')
                )
            except:
                return self.error_response('Ошибка при сохранении ответа')

            subject_models.SubjectToPsychoTestAnswer.objects \
                .filter(
                    subject_test=subject_test,
                    answer__test_question_id=serializer.validated_data['question_id']
                ).delete()

            subject_models.SubjectToPsychoTestAnswer.objects \
                .create(
                    subject_test=subject_test,
                    answer=new_answer
                )

            return self.success_response()

        if serializer.validated_data.get('answer_ids'):
            try:
                new_answers = models.PsychoTestQuestionToAnswer.objects.get(
                        id=serializer.validated_data.get('answer_id')
                    )
            except:
                return self.error_response('Ошибка при сохранении ответа')

            subject_models.SubjectToPsychoTestAnswer.objects \
                .filter(
                    subject_test=subject_test,
                    answer__test_question_id=serializer.validated_data['question_id']
                ).delete()

            to_bulk = [
                subject_models.SubjectToPsychoTestAnswer(subject_test=subject_test, answer=a)
                for a in new_answers
            ]

            subject_models.SubjectToPsychoTestAnswer.objects.bulk_create(to_bulk, ignore_conflicts=True)

            return self.success_response()

        return self.error_response('')



