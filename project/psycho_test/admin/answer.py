from django.contrib import admin
from psycho_test.models.answer import Answer, AnswerScore, AnswerScoreAction
from utils.admins import BaseModelAdmin


@admin.register(Answer)
class AnswerAdmin(BaseModelAdmin):
    list_display = ('id', 'title', 'created_at')


@admin.register(AnswerScore)
class AnswerScoreAdmin(BaseModelAdmin):
    list_display = ('id', 'action', 'value')


@admin.register(AnswerScoreAction)
class AnswerScoreActionAdmin(BaseModelAdmin):
    list_display = ('id', 'name', 'code', 'created_at')