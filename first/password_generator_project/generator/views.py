import random

from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    # return HttpResponse('Hello')
    lst = list(range(6, 15))
    return render(request, 'generator/home.html', {'lst': lst})

def password(request):
    char = [chr(i) for i in range(97, 123)]

    if request.GET.get('uppercase'):
        char.extend([chr(i) for i in range(65, 91)])

    if request.GET.get('numbers'):
        char.extend([chr(i) for i in range(48, 58)])

    if request.GET.get('special'):
        char.extend([chr(i) for i in range(33, 48)])

    length = int(request.GET.get('length'))
    psw = ''
    for i in range(length):
        psw += random.choice(char)
    return render(request, 'generator/password.html', {'password': psw})

def page(request):
    return render(request, 'generator/page.html')



