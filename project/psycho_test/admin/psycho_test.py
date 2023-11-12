from django.contrib import admin
from django.utils.safestring import mark_safe

from psycho_test.models.psycho_test import PsychoTestQuestionToAnswer, PsychoTest, PsychoTestToQuestion
from psycho_test.models.result import PsychoTestToResult
from utils.admins import BaseModelAdmin


class PsychoTestToResultInline(admin.TabularInline):
    model = PsychoTestToResult
    extra = 0
    min_num = 0


@admin.register(PsychoTest)
class PsychoTestAdmin(BaseModelAdmin):
    def questions_count(self, obj):
        return PsychoTestToQuestion.objects.filter(psycho_test_id=obj.id).count()

    questions_count.short_description = 'Кол-во вопросов'

    inlines = (PsychoTestToResultInline,)
    list_display = ('id', 'name', 'questions_count', 'created_at')


class PsychoTestQuestionToAnswerInline(admin.TabularInline):
    model = PsychoTestQuestionToAnswer
    extra = 0
    min_num = 0


@admin.register(PsychoTestToQuestion)
class PsychoTestToQuestionAdmin(BaseModelAdmin):
    inlines = (PsychoTestQuestionToAnswerInline, )
    list_display = ('id', 'psycho_test', 'question', 'created_at')


@admin.register(PsychoTestQuestionToAnswer)
class PsychoTestQuestionToAnswerAdmin(BaseModelAdmin):

    def br_test_question(self, obj):
        return mark_safe(f"Тест: {obj.test_question.psycho_test.name} <br/><br/> Вопрос: {obj.test_question.question.title}")

    br_test_question.allow_tags = True
    br_test_question.short_description = 'Связь тестирования с вопросом'

    list_display = ('id', 'br_test_question', 'answer', 'score', 'created_at')
