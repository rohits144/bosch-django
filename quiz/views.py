from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .models import Quiz, Option, Scores
from .forms import createQuestionForm
from .serializers import quizSerializer, optionSerializer
import logging

logger = logging.getLogger(__name__)

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.data)
        if form.is_valid():
            form.save()
            redirect("home")
    elif request.method == "GET":
        form = UserCreationForm()
        context = {
            "form": form
        }
        render(request, "templates/quiz/login.html", context)


def display_all_quiz(request):
    all_questions = Quiz.Objects.all()
    context = {
        "questions": all_questions
    }
    render(request, "templates/quiz/questions.html", context)


def create_question(request):
    if request.method == "GET":
        form = createQuestionForm()
        context = {
            "form": form
        }
        render(request, "templates/quiz/create_question.html", context)

    elif request.method == "POST":
        form = createQuestionForm(request.data)
        if form.is_valid():
            form_dict = form.cleaned_data()
            question = form_dict['question']
            author = form_dict['author']
            correct_option = form_dict['correct_option']
            option1 = form_dict["option1"]
            option2 = form_dict["option2"]
            option3 = form_dict["option3"]
            option4 = form_dict["option4"]
            optn_dict = {
                "option1": option1,
                "option2": option2,
                "option3": option3,
                "option4": option4
            }

            quiz_dict = {"question": question, "author": author, "correct_option": correct_option}

            serializer1 = quizSerializer(data=quiz_dict)
            if serializer1.is_valid():
                serializer1.save()

            for i in range(1, 5):
                option_dict = {"option_statement": optn_dict["option" + str(i)], "belongs_to": author}
                serializer2 = optionSerializer(data=option_dict)
                if serializer2.is_valid():
                    serializer2.save()

            redirect("home")


def validate_quiz(request):
    dict = request.data
    author = dict['user_id']
    question_id = dict["question_id"]
    selected_option = dict['option']
    correct_option = Quiz.objects.get(id = question_id).correct_option
    if correct_option == selected_option:
        try:
            score_obj = Scores.objects.get(user = author)
        except Exception as e:
            logger.info("User's score not found")

        score = score_obj.total_user_score
        score +=1
        score_obj.total_user_score = score
        score_obj.save()


