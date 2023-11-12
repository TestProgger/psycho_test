from django.db import models
from utils.models import AbsractDictionaryModel, AbstractBaseModel


class QuestionType(AbsractDictionaryModel):
    class Meta:
        verbose_name = "Вопрос: Тип"
        verbose_name_plural = "Вопросы: Типы"
        ordering = ['name', ]


class Question(AbstractBaseModel):
    title = models.TextField(
        verbose_name="Текст вопроса"
    )

    description = models.TextField(
        null=True,
        blank=True,
        verbose_name="Описание"
    )

    type = models.ForeignKey(
        to="psycho_test.QuestionType",
        on_delete=models.PROTECT,
        verbose_name="Тип вопроса"
    )

    def __str__(self):
        return f"{self.title} - {self.type.name}"

    class Meta:
        verbose_name = "Вопрос"
        verbose_name_plural = "Вопросы"
        ordering = ['title', ]