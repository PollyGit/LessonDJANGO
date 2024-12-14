from django.shortcuts import render, redirect
# импорт таблицы
from .models import News_post

from .forms import News_postForm
# Create your views here.

def home(request):
	#Берем все новости и сохраняем в переменную news
	news = News_post.objects.all()
	#{'news': news} вся информация передается в виде словаря
	return render(request, 'news/news.html', {'news': news})


def create_news(request):
	#Добавляем проверку на метод POST/GET.
	# Переменную error размещаем выше, чтобы она изначально имела пустое значение.
	error = ''
	if request.method == 'POST':
		form = News_postForm(request.POST)  # Сюда сохранится информация от пользователя.
		if form.is_valid():
			form.save()
			return redirect('news_home')
		else:
			error = "Данные были заполнены некорректно"
		#СОздание объекта класса и передадим его в шаблон
	form = News_postForm()
	return render(request, 'news/add_new_post.html', {'form': form, 'error': error})