from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("publication date")


class User(models.Model):
    user_name = models.CharField(max_lengt=64)


class Answer(models.Model):
    answer_text = models.CharField(max_length=500)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    votes = models.IntegerField(default=0)


class Votes(models.Model):
    raise NotImplementedError




