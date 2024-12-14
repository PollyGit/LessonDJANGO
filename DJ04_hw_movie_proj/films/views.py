from django.shortcuts import render, redirect

from .forms import Films_postForm
# импорт таблицы
from .models import Films_post


def index(request):
    # Берем все фильмы и сохраняем в переменную news
    films = Films_post.objects.all()
    # {'news': news} вся информация передается в виде словаря
    # путь внутри папки templates:
    return render(request, 'films/index.html', {'films': films})
    # return HttpResponse("<h1>Это мой первый проект на Django</h1>")


def page2(request):
    # Добавляем проверку на метод POST/GET.
    # Переменную error размещаем выше, чтобы она изначально имела пустое значение.
    error = ''
    if request.method == 'POST':
        form = Films_postForm(request.POST)  # Сюда сохранится информация от пользователя.
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = "Данные были заполнены некорректно"
    # СОздание объекта класса и передадим его в шаблон
    form = Films_postForm()
    return render(request, 'films/page2.html', {'form': form, 'error': error})
