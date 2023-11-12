from django.db import models
from utils.models import AbsractDictionaryModel, AbstractBaseModel


class PsychoTestResultDictionary(AbsractDictionaryModel):
    description = models.TextField(
        null=True,
        blank=True,
        verbose_name="Описание"
    )

    class Meta:
        verbose_name = "Результат тестирования: Справочник"
        verbose_name_plural = "Результаты тестирования: Справочник"
        ordering = ['name', ]


class PsychoTestToResult(AbstractBaseModel):
    psycho_test = models.ForeignKey(
        to="psycho_test.PsychoTest",
        on_delete=models.PROTECT,
        verbose_name="Психологический тест"
    )

    result = models.ForeignKey(
        to="psycho_test.PsychoTestResultDictionary",
        on_delete=models.PROTECT,
        verbose_name="Результат"
    )

    score_min = models.FloatField(
        default=0.0,
        verbose_name="Минимальное количество баллов"
    )

    score_max = models.FloatField(
        default=0.0,
        verbose_name="Максимальное количество баллов"
    )

    def __str__(self):
        return f"{self.psycho_test.name} - {self.result.name}"

    class Meta:
        verbose_name = "Результат тестирования"
        verbose_name_plural = "Результаты тестирования"

