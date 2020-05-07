from rest_framework import serializers
from .models import Quiz, Option


class quizSerializer(serializers.Modelserializer):
    class Meta:
        model = Quiz
        fields = ["question", "author", "correct_option", "creation_time"]

    def save(self, data):
        quiz_obj = Quiz(data["question"], data["author"], data["correct_option"])
        quiz_obj.save()


class optionSerializer(serializers.Modelserializer):
    class Meta:
        model = Option
        fields = ["option_statement", "belongs_to"]

    def save(self, data):
        quiz_obj = Option(data["option_statement"], data["author"])
        quiz_obj.save()
