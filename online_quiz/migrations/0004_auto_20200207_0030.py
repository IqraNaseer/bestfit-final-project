# Generated by Django 3.0.2 on 2020-02-06 19:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('online_quiz', '0003_auto_20200207_0030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reporting',
            name='user_result',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='online_quiz.ResultsPredictions'),
        ),
    ]
