# Generated by Django 4.2.7 on 2023-11-05 19:50

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('subject', '0002_subjecttopsychotest'),
    ]

    operations = [
        migrations.AddField(
            model_name='subjectidentity',
            name='expires',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]