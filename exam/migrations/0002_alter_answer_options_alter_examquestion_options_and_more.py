# Generated by Django 4.1.1 on 2023-05-05 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='answer',
            options={'verbose_name_plural': 'Multiple Choice Answers'},
        ),
        migrations.AlterModelOptions(
            name='examquestion',
            options={'verbose_name_plural': 'Multiple Choice Exam Questions'},
        ),
        migrations.AlterModelOptions(
            name='structuredquestion',
            options={'verbose_name_plural': 'Structured Exam Questions'},
        ),
        migrations.AlterField(
            model_name='exam',
            name='endtime',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='exam',
            name='start_time',
            field=models.CharField(max_length=100),
        ),
    ]
