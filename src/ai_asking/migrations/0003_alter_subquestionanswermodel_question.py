# Generated by Django 3.2.5 on 2023-02-08 09:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ai_asking', '0002_questionmodel_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subquestionanswermodel',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sub_question_answer', to='ai_asking.questionmodel'),
        ),
    ]
