from django.urls import path
from . import views as quiz_view

urlpatterns = [
    path('home/', quiz_view.display_all_quiz, name="home"),
    path("createQuestion", quiz_view.create_question, name="create"),
    path("validateQuiz", quiz_view.validate_quiz, name="validate")
]
