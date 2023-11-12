from django.contrib import admin
from psycho_test.models.psycho_test import PsychoTestQuestionToAnswer, PsychoTest, PsychoTestToQuestion
from psycho_test.models.result import PsychoTestToResult
from utils.admins import BaseModelAdmin


class PsychoTestToResultInline(admin.TabularInline):
    model = PsychoTestToResult
    extra = 0
    min_num = 0


@admin.register(PsychoTest)
class PsychoTestAdmin(BaseModelAdmin):
    inlines = (PsychoTestToResultInline, )
    list_display = ('id', 'name', 'created_at')


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
    list_display = ('id', 'test_question', 'answer', 'score', 'created_at')