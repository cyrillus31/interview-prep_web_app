# Generated by Django 5.0.1 on 2024-01-11 12:19

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("flashcards", "0002_answer_author_answer_pub_date_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="answer",
            name="language",
            field=models.CharField(
                blank=True,
                choices=[("EN", "English"), ("RU", "Russian")],
                max_length=3,
                null=True,
            ),
        ),
        migrations.AddField(
            model_name="question",
            name="author",
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name="question",
            name="language",
            field=models.CharField(
                blank=True,
                choices=[("EN", "English"), ("RU", "Russian")],
                max_length=3,
                null=True,
            ),
        ),
        migrations.AddField(
            model_name="question",
            name="votes",
            field=models.IntegerField(default=0),
        ),
    ]