from django.urls import path

# импортируем views.py из этой же папки
from . import views

# подключаем файл views.py для отображения страниц HTML
# index - ф-ция из views.py которая будет выполняться при
# переходе на главную страницу проекта
urlpatterns = [
    path('', views.index, name='home'),
    path('new', views.new, name='page2'),
    path('page3', views.page3, name='page3'),
    path('page4', views.page4, name='page4'),
    path('data', views.data),
    path('test', views.test)
]
