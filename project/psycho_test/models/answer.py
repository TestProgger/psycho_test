from django.db import models
from utils.models import AbsractDictionaryModel, AbstractBaseModel


class Answer(AbstractBaseModel):
    title = models.TextField(
        verbose_name="Текст вопроса"
    )

    description = models.TextField(
        null=True,
        blank=True,
        verbose_name="Описание"
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Ответ"
        verbose_name_plural = "Ответы"
        ordering = ['title', ]


class AnswerScore(AbstractBaseModel):
    action = models.ForeignKey(
        to="psycho_test.AnswerScoreAction",
        on_delete=models.CASCADE,
        verbose_name="Действие"
    )

    value = models.FloatField(
        default=0,
        verbose_name="Количество"
    )

    def __str__(self):
        return f"{self.action.name} {self.value}"

    class Meta:
        verbose_name = "Ответ: Баллы"
        verbose_name_plural = "Ответы: Баллы"
        ordering = ['created_at', ]


class AnswerScoreAction(AbsractDictionaryModel):
    class Meta:
        verbose_name = "Ответ: Действия с баллами"
        verbose_name_plural = "Ответы: Действия с баллами"
        ordering = ['name', ]