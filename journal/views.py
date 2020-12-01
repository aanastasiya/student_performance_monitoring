from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout

from .models import Student, Subject, Grade, Professor, Department
from .users_creation import StudentCreationForm


def journal(request):
    return render(request, 'journal/list.html')


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()

            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)

            return redirect('journal')
    else:
        form = UserCreationForm()
    context = {'form': form}

    return render(request, 'registration/register.html', context)


def logout(request):
    logout(request)
