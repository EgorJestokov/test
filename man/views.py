from django.shortcuts import render, redirect
from django.contrib import messages
from email import message
from multiprocessing import context
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login, logout
from .forms import CreateUserForm


def home(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request, 'man/home.html')


def login_user(request):

    page = 'login'

    # Проверка авторизованности пользователя.
    # Если True, то переадресует на домашнюю страницу
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

        # Блок для отлавливания ошибки
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'Такой пользователь не существует')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Имя пользователя или пароль введены неверно')

    context = {'page': page}
    return render(request, 'man/login.html', context)


def logout_user(request):
    logout(request)
    return redirect('home')


def register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('home')
    context = {'form': form}
    return render(request, 'man/registration.html', context)


def reports(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request, 'man/reports.html', {'title': 'Отчеты'})


def manual(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request, 'man/manual.html', {'title': 'Справочник'})


def main(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request, 'man/main.html', {'title': 'good'})
