from django.shortcuts import render, HttpResponse


from . import models


def index(request):
    context = {
            "username": "Cyrillus",
            "questions": [q.question_text for q in models.Question.objects.all()]
            }
    return render(request, "index.html", context)
