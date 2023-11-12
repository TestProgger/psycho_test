# Generated by Django 4.2.7 on 2023-11-12 19:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('psycho_test', '0002_alter_answer_options_alter_answerscore_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='psychotest',
            name='is_visible',
            field=models.BooleanField(default=True, verbose_name='Виден'),
        ),
        migrations.AlterField(
            model_name='answer',
            name='title',
            field=models.TextField(verbose_name='Текст ответа'),
        ),
        migrations.AlterField(
            model_name='psychotestquestiontoanswer',
            name='test_question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='psycho_test.psychotesttoquestion', verbose_name='Связь тестирования с вопросом'),
        ),
    ]
