from django import forms
from .models import Quiz


class createQuestionForm(forms.ModelForm):

    option1 = forms.CharField(max_length=100)
    option2 = forms.CharField(max_length=100)
    option3 = forms.CharField(max_length=100)
    option4 = forms.CharField(max_length=100)

    class Meta:
        model = Quiz
        fields = ["question", "author", "correct_option", "option1", "option2", "option3", "option4"]