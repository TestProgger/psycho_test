# Generated by Django 4.2.7 on 2023-11-15 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subject', '0008_alter_subjectidentity_secret_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subjecttopsychotest',
            name='token',
            field=models.CharField(max_length=255, verbose_name='Токен доступа'),
        ),
    ]