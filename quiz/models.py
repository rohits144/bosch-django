from django.db import models
from django.contrib.auth.models import User


class Quiz(models.Model):
    """
    This class wll save quiz and its options
    """

    question = models.CharField(max_length=500, blank=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE())
    creation_time = models.TimeField(auto_now_add=True)
    correct_option = models.IntegerField(max_length=1,blank=False)
    ordering = ["-creation_time"]


class Option(models.Model):
    quiz = models.ManyToOneRel(Quiz)
    option_statement = models.CharField(max_length=100)
    belongs_to = models.ForeignKey(Quiz, on_delete=models.CASCADE())
    creation_time = models.TimeField()


class Scores(models.Model):
    total_user_score = models.IntegerField(default=0,)
    last_modified = models.TimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE())