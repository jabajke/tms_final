from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth import authenticate, login


def index(request):
    data = {
        'title': 'Главная страница',
        }
    return render(request, 'main/index.html', data)


def about(request):
    return render(request, 'main/about.html')


def create(request):
    return render(request, 'news/create.html')



