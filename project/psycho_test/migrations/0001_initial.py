# Generated by Django 4.2.7 on 2023-11-05 18:24

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.TextField(verbose_name='Текст вопроса')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Ответ',
                'verbose_name_plural': 'Ответы',
            },
        ),
        migrations.CreateModel(
            name='AnswerScore',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('value', models.FloatField(default=0, verbose_name='Количество')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AnswerScoreAction',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255, verbose_name='Наименование')),
                ('code', models.CharField(db_index=True, max_length=255, unique=True, verbose_name='Код')),
            ],
            options={
                'verbose_name': 'Действия с баллами',
                'verbose_name_plural': 'Действия с баллами',
            },
        ),
        migrations.CreateModel(
            name='PsychoTest',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255, verbose_name='Наименование')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('image_url', models.TextField(blank=True, null=True, verbose_name='Ссылка на изображение')),
            ],
            options={
                'verbose_name': 'Психологический тест',
                'verbose_name_plural': 'Психологические тесты',
            },
        ),
        migrations.CreateModel(
            name='PsychoTestResultDictionary',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255, verbose_name='Наименование')),
                ('code', models.CharField(db_index=True, max_length=255, unique=True, verbose_name='Код')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Справочник: Результат тестирования',
                'verbose_name_plural': 'Справочник: Результаты тестирования',
            },
        ),
        migrations.CreateModel(
            name='QuestionType',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255, verbose_name='Наименование')),
                ('code', models.CharField(db_index=True, max_length=255, unique=True, verbose_name='Код')),
            ],
            options={
                'verbose_name': 'Тип вопроса',
                'verbose_name_plural': 'Типы вопросов',
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.TextField(verbose_name='Текст вопроса')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='psycho_test.questiontype', verbose_name='Тип вопроса')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PsychoTestToResult',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('score_min', models.FloatField(default=0.0, verbose_name='Минимальное количество баллов')),
                ('score_max', models.FloatField(default=0.0, verbose_name='Максимальное количество баллов')),
                ('psycho_test', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='psycho_test.psychotest', verbose_name='Психологический тест')),
                ('result', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='psycho_test.psychotestresultdictionary', verbose_name='Результат')),
            ],
            options={
                'verbose_name': 'Результат тестирования',
                'verbose_name_plural': 'Результаты тестирования',
            },
        ),
        migrations.CreateModel(
            name='PsychoTestToQuestion',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('psycho_test', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='psycho_test.psychotest', verbose_name='Психологический тест')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='psycho_test.question', verbose_name='Вопрос')),
            ],
            options={
                'verbose_name': 'Связь тестирования с вопросом',
                'verbose_name_plural': 'Связь тестирования с вопросом',
            },
        ),
        migrations.CreateModel(
            name='PsychoTestQuestionToAnswer',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('answer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='psycho_test.answer', verbose_name='Ответ')),
                ('score', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='psycho_test.answerscore', verbose_name='Баллы')),
                ('test_question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='psycho_test.psychotesttoquestion')),
            ],
            options={
                'verbose_name': 'Связь теста с ответом',
                'verbose_name_plural': 'Связь теста с ответами',
            },
        ),
        migrations.AddField(
            model_name='answerscore',
            name='action',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='psycho_test.answerscoreaction', verbose_name='Действие'),
        ),
    ]