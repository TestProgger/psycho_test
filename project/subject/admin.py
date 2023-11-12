from django.contrib import admin
from subject.models import Subject, SubjectGroup, SubjectToPsychoTestAnswer, SubjectToPsychoTestResult
from utils.admins import BaseModelAdmin


@admin.register(Subject)
class SubjectAdmin(BaseModelAdmin):
    list_display = ("id", "first_name", "last_name", "middle_name", "group", "created_at")
    search_fields = ('first_name', 'last_name', 'middle_name')


@admin.register(SubjectGroup)
class SubjectGroupAdmin(BaseModelAdmin):
    list_display = ('id', 'name', 'code', 'created_at')
    search_fields = ('name', 'code')


@admin.register(SubjectToPsychoTestAnswer)
class SubjectToPsychoTestAnswerAdmin(BaseModelAdmin):
    list_display = ('id', 'subject_test', 'answer', 'created_at')

    def _get_user_defined_readonly_fields(self, request, obj=None):
        return ('subject_test', 'answer')


@admin.register(SubjectToPsychoTestResult)
class SubjectToPsychoTestResultAdmin(BaseModelAdmin):
    list_display = ('id', 'subject', 'result', 'created_at')
    readonly_fields = ('id', 'created_at', 'updated_at', 'token')
