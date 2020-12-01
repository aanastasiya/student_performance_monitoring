from django.contrib.auth.forms import UserCreationForm
from django import forms

from journal.models import Student


class StudentCreationForm(UserCreationForm):
    class Meta:
        model = Student
        fields = ['name', 'surname', 'patronymic', 'year', 'faculty', 'specialty', 'group']
