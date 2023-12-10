from django.shortcuts import render

def signupuser(request):
    return render(request, 'todo/singnupuser.html')


def currenttodos(request):
    return render(request, 'todo/currenttodos.html')

