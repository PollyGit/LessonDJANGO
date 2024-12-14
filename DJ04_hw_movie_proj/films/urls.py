from django.urls import path

# импортируем views.py из этой же папки
from . import views

# подключаем файл views.py для отображения страниц HTML
# index - ф-ция из views.py которая будет выполняться при
# переходе на главную страницу проекта
urlpatterns = [
    path('', views.index, name='home'),
    path('page2', views.page2, name='page2'),
]
