from django.shortcuts import render
# импорт таблицы
from .models import News_post
# Create your views here.

def home(request):
	#Берем все новости и сохраняем в переменную news
	news = News_post.objects.all()
	#{'news': news} вся информация передается в виде словаря
	return render(request, 'news/news.html', {'news': news})