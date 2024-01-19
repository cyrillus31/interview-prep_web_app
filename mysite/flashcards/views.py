from django.shortcuts import render, HttpResponse, get_object_or_404


from . import models


def index(request):
    context = {
            "username": "Cyrillus",
            "questions": [(q.id, q.question_text) for q in models.Question.objects.all()]
            }
    return render(request, "flashcards/index.html", context)


def flashcards(request, question_id: int):
    question = get_object_or_404(models.Question, pk=question_id)
    context = {
            "question": question.question_text,
            }
    return render(request, "flashcards/flashcard.html", context)


