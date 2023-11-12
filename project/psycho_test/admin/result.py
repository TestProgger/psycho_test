from django.contrib import admin
from psycho_test.models.result import PsychoTestToResult, PsychoTestResultDictionary
from utils.admins import BaseModelAdmin


@admin.register(PsychoTestResultDictionary)
class PsychoTestResultDictionaryAdmin(BaseModelAdmin):
    list_display = ('id', 'name', 'code')


@admin.register(PsychoTestToResult)
class PsychoTestToResultAdmin(BaseModelAdmin):
    list_display = ('id', 'psycho_test', 'result', 'score_min', 'score_max')