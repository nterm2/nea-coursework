# Generated by Django 4.1.5 on 2023-01-21 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_quiz', '0002_alter_timestable_average_percentage_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=200)),
                ('option_1', models.IntegerField()),
                ('option_2', models.IntegerField()),
                ('option_3', models.IntegerField()),
                ('option_4', models.IntegerField()),
                ('answer', models.IntegerField()),
            ],
        ),
    ]
