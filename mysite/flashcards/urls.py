from django.contrib import admin
from django.urls import path

from . import views

app_name = "flashcards"

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:question_id>/", views.flashcards, name="flashcards"),
]
