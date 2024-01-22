from django.db import models
from django.utils import choices, timezone
from django.conf import settings


LANGUAGE_CHOICE = {
        "EN": "English",
        "RU": "Russian",
        }
        

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    pub_date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    language = models.CharField(max_length=3, choices=LANGUAGE_CHOICE, null=True, blank=True)
    deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.question_text


class Answer(models.Model):
    answer_text = models.CharField(max_length=500)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    votes = models.IntegerField(default=0)
    pub_date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    language = models.CharField(max_length=3, choices=LANGUAGE_CHOICE, null=True, blank=True)
    deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.answer_text

