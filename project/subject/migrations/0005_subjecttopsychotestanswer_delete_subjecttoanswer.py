# Generated by Django 4.2.7 on 2023-11-05 21:03

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('psycho_test', '0002_alter_answer_options_alter_answerscore_options_and_more'),
        ('subject', '0004_subjecttopsychotest_token'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubjectToPsychoTestAnswer',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('answer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='psycho_test.psychotestquestiontoanswer', verbose_name='Ответ')),
                ('subject_test', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='subject.subjecttopsychotestanswer', verbose_name='Объект тестирования')),
            ],
            options={
                'verbose_name': 'Связь объекта тестирования с ответом',
                'verbose_name_plural': 'Связь объекта тестирования с ответом',
            },
        ),
        migrations.DeleteModel(
            name='SubjectToAnswer',
        ),
    ]