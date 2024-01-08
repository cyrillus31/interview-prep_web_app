from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("publication date")


    def __str__(self):
        return self.question_text


class Answer(models.Model):
    answer_text = models.CharField(max_length=500)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    votes = models.IntegerField(default=0)


    def __str__(self):
        return self.answer_text
