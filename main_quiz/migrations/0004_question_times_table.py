# Generated by Django 4.1.5 on 2023-01-21 10:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_quiz', '0003_question'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='times_table',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main_quiz.timestable'),
        ),
    ]
