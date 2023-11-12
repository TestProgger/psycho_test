from django.db import models
from django.utils import timezone

from utils.models import AbstractBaseModel, AbsractDictionaryModel


class SubjectGroup(AbsractDictionaryModel):

    description = models.TextField(
        null=True,
        blank=True,
        verbose_name="Описание"
    )

    def __str__(self):
        return f"{self.name} - {self.code}"

    class Meta:
        verbose_name = "Группа"
        verbose_name_plural = "Группы"


class Subject(AbstractBaseModel):
    first_name = models.CharField(
        max_length=255,
        verbose_name="Имя"
    )

    last_name = models.CharField(
        max_length=255,
        verbose_name="Фамилия"
    )

    middle_name = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name="Отчество"
    )

    group = models.ForeignKey(
        to="subject.SubjectGroup",
        on_delete=models.PROTECT,
        verbose_name="Группа"
    )

    def __str__(self):
        return f"{self.last_name} {self.first_name} {self.middle_name or ''}".strip()

    class Meta:
        verbose_name = "Объект тестирования"
        verbose_name_plural = "Объекты тестирования"


class SubjectIdentity(AbstractBaseModel):
    subject = models.ForeignKey(
        to="subject.Subject",
        on_delete=models.CASCADE,
        verbose_name="Объект тестирования"
    )

    secret = models.CharField(
        max_length=64,
    )

    token = models.CharField(
        max_length=64
    )

    expires = models.DateTimeField(
        default=timezone.now
    )

    class Meta:
        verbose_name = "Идентификатор объекта тестирования"
        verbose_name_plural = "Идентификаторы объектов тестирования"


class SubjectToPsychoTestResult(AbstractBaseModel):
    subject = models.ForeignKey(
        to="subject.Subject",
        on_delete=models.CASCADE,
        verbose_name="Объект исследования"
    )

    result = models.ForeignKey(
        to="psycho_test.PsychoTestToResult",
        on_delete=models.PROTECT,
        verbose_name="Результат"
    )

    token = models.CharField(
        max_length=255,
        verbose_name="Токен доступа к результату"
    )

    class Meta:
        verbose_name = "Результат тестирования"
        verbose_name_plural = "Результаты тестирования"


class SubjectToPsychoTestAnswer(AbstractBaseModel):
    subject_test = models.ForeignKey(
        to="subject.SubjectToPsychoTest",
        on_delete=models.CASCADE,
        verbose_name="Объект тестирования"
    )

    answer = models.ForeignKey(
        to="psycho_test.PsychoTestQuestionToAnswer",
        on_delete=models.PROTECT,
        verbose_name="Ответ"
    )

    class Meta:
        verbose_name = "Связь объекта тестирования с ответом"
        verbose_name_plural = "Связь объекта тестирования с ответом"


class SubjectToPsychoTest(AbstractBaseModel):
    subject = models.ForeignKey(
        to="subject.Subject",
        on_delete=models.CASCADE,
        verbose_name="Объект тестирования"
    )

    psycho_test = models.ForeignKey(
        to="psycho_test.PsychoTest",
        on_delete=models.CASCADE,
        verbose_name="Психологический тест"
    )

    is_completed = models.BooleanField(
        default=False,
        verbose_name="Завершен"
    )

    token = models.CharField(
        max_length=80,
        verbose_name="Токен доступа"
    )

    def __str__(self):
        return f"{self.subject}  - {self.psycho_test}"

    class Meta:
        verbose_name = "Связь объекта тестирования с тестом"
        verbose_name_plural = "Связь объекта тестирования с тестом"