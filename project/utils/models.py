from django.db import models
import uuid


class AbstractBaseModel(models.Model):
    id = models.UUIDField(
        primary_key=True,
        unique=True,
        default=uuid.uuid4,
        editable=False,
        verbose_name="ID"
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата создания"
    )

    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Дата обновления"
    )

    class Meta:
        abstract = True


class AbsractDictionaryModel(AbstractBaseModel):
    name = models.CharField(
        max_length=255,
        verbose_name="Наименование"
    )

    code = models.CharField(
        max_length=255,
        db_index=True,
        verbose_name="Код",
        unique=True
    )

    def __str__(self):
        return f"{self.name} - {self.code}"

    class Meta:
        abstract = True