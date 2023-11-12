# Generated by Django 4.2.7 on 2023-11-05 18:24

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('psycho_test', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('first_name', models.CharField(max_length=255, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=255, verbose_name='Фамилия')),
                ('middle_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Отчество')),
            ],
            options={
                'verbose_name': 'Объект тестирования',
                'verbose_name_plural': 'Объекты тестирования',
            },
        ),
        migrations.CreateModel(
            name='SubjectGroup',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255, verbose_name='Наименование')),
                ('code', models.CharField(db_index=True, max_length=255, unique=True, verbose_name='Код')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Группа',
                'verbose_name_plural': 'Группы',
            },
        ),
        migrations.CreateModel(
            name='SubjectToPsychoTestResult',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('token', models.CharField(max_length=255, verbose_name='Токен доступа к результату')),
                ('result', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='psycho_test.psychotesttoresult', verbose_name='Результат')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='subject.subject', verbose_name='Объект исследования')),
            ],
            options={
                'verbose_name': 'Результат тестирования',
                'verbose_name_plural': 'Результаты тестирования',
            },
        ),
        migrations.CreateModel(
            name='SubjectToAnswer',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('answer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='psycho_test.psychotestquestiontoanswer', verbose_name='Ответ')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='subject.subject', verbose_name='Объект тестирования')),
            ],
            options={
                'verbose_name': 'Связь объекта тестирования с ответом',
                'verbose_name_plural': 'Связь объекта тестирования с ответом',
            },
        ),
        migrations.CreateModel(
            name='SubjectIdentity',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('secret', models.CharField(max_length=64)),
                ('token', models.CharField(max_length=64)),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='subject.subject', verbose_name='Объект тестирования')),
            ],
            options={
                'verbose_name': 'Идентификатор объекта тестирования',
                'verbose_name_plural': 'Идентификаторы объектов тестирования',
            },
        ),
        migrations.AddField(
            model_name='subject',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='subject.subjectgroup', verbose_name='Группа'),
        ),
    ]
