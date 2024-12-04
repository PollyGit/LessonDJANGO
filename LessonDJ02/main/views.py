# Create your views here.

# класс HttpResponse позволяет нам возвращать HTTP-ответы
from django.http import HttpResponse
from django.shortcuts import render


# создать функцию, которая будет выполняться при
# переходе на главную страницу проекта
#
# функция index принимает один обязательный параметр — request.
# Этот параметр содержит информацию о текущем HTTP-запросем
def index(request):
    # return HttpResponse("<h1>Это мой первый проект на Django</h1>")
    #путь внутри папки templates:
    return render(request, 'main/index.html', {'caption':"CatDjango"})


def new(request):
    # return HttpResponse("<h1>Это вторая страница моего проекта на Django</h1>")
    return render(request, 'main/new.html')

def page3(request):
    #путь внутри папки templates:
    return render(request, 'main/page3.html')


def page4(request):
    #путь внутри папки templates:
    return render(request, 'main/page4.html')


def data(request):
    return HttpResponse("<h1>Это вторая страница с интересной информацией</h1>")


def test(request):
    # Внутри функции мы используем HttpResponse для создания и
    # возврата ответа с HTML-кодом.
    return HttpResponse("<h1>Это тестовая страница моего проекта на Django</h1>")
