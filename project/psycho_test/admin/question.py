from django.contrib import admin
from psycho_test.models.question import QuestionType, Question
from utils.admins import BaseModelAdmin


@admin.register(Question)
class QuestionAdmin(BaseModelAdmin):
    list_display = ('id', 'title', 'type', 'created_at')


@admin.register(QuestionType)
class QuestionTypeAdmin(BaseModelAdmin):
    list_display = ('id', 'name', 'code')