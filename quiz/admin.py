from django.contrib import admin
from .models import Quiz,Option
admin.sites.register(Quiz)
admin.sites.register(Option)