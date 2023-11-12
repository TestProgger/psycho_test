from django.db import models
from utils.models import AbstractBaseModel


class PsychoTest(AbstractBaseModel):
    name = models.CharField(
        max_length=255,
        verbose_name="Наименование"
    )

    description = models.TextField(
        null=True,
        blank=True,
        verbose_name="Описание"
    )

    image_url = models.TextField(
        null=True,
        blank=True,
        verbose_name="Ссылка на изображение"
    )

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Психологический тест"
        verbose_name_plural = "Психологические тесты"
        ordering = ['name', ]


class PsychoTestToQuestion(AbstractBaseModel):

    psycho_test = models.ForeignKey(
        to="psycho_test.PsychoTest",
        on_delete=models.CASCADE,
        verbose_name="Психологический тест"
    )

    question = models.ForeignKey(
        to="psycho_test.Question",
        on_delete=models.CASCADE,
        verbose_name="Вопрос",
    )

    def __str__(self):
        return f"{self.psycho_test.name} - {self.question.title}"

    class Meta:
        verbose_name = "Психологический тест: Связь тестирования с вопросом"
        verbose_name_plural = "Психологические тесты: Связь тестирования с вопросом"
        ordering = ['created_at', ]


class PsychoTestQuestionToAnswer(AbstractBaseModel):
    test_question = models.ForeignKey(
        to="psycho_test.PsychoTestToQuestion",
        on_delete=models.CASCADE,
        verbose_name='Связь тестирования с вопросом'
    )

    answer = models.ForeignKey(
        to="psycho_test.Answer",
        on_delete=models.CASCADE,
        verbose_name="Ответ"
    )

    score = models.ForeignKey(
        to="psycho_test.AnswerScore",
        on_delete=models.CASCADE,
        verbose_name="Баллы"
    )

    def __str__(self):
        return f"{self.test_question.psycho_test.name} - {self.test_question.question.title} - {self.answer.title}"

    class Meta:
        verbose_name = "Психологический тест: Связь теста с ответом"
        verbose_name_plural = "Психологические тесты: Связь теста с ответами"
        ordering = ['created_at', ]