# Generated by Django 4.1.5 on 2023-01-28 22:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main_quiz', '0006_rename_eight_tt_questionoverview_eight_times_table_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='questionoverview',
            name='owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
