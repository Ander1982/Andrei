from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from .forms import ExForm


def home(request):
    return render(request, 'porol/home.html')


def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')


def worker(request):
    return render(request, 'porol/worker.html')


def reguser(request):
    if request.method == 'GET':
        return render(request, 'porol/reguser.html', {'form': UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('worker')
            except IntegrityError:
                return render(request, 'porol/reguser.html', {'form': UserCreationForm(),
                                                           'error': 'Такое имя пользователя существует, создайте новое'})
        else:
            return render(request, 'porol/reguser.html', {'form': UserCreationForm(), 'error': 'Пароли не совпадают'})

def loginuser(request):
    if request.method == 'GET':
        return render(request, 'porol/loginuser.html', {'form': AuthenticationForm})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'porol/loginuser.html', {
                'form': AuthenticationForm,
                'error': 'Неверные данные для входа'})
        else:
            login(request, user)
            return redirect('worker')


def creatework(request):
    if request.method == "GET":
        return render(request, 'porol/creatework.html', {'form': ExForm()})
    else:
        try:
            form = ExForm(request.POST)
            new = form.save(commit=False)
            new.user = request.user
            new.save()
            return redirect('worker')
        except ValueError:
            return render(request, 'porol/creatework.html', {
                'form': ExForm(),
                'error': 'Переданы неверные данные, Попробуйте еще раз'})
