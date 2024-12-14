from django.db import models

# Create your models here.

# Создать класс для работы с БД
# models.Model - название класса от кот-го наследуется
class Films_post(models.Model):
    title = models.CharField('Название фильма', max_length=70)
    short_description = models.TextField('Описание фильма')
    text = models.TextField('Отзыв')


    #прописываем специальный метод внутри класса,
    # чтобы на сайте отображалось название новости.
    def __str__(self):
        return self.title


    #создаём вложенный класс Meta,
    # чтобы дать русские названия таблице Films_post
    class Meta:
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'


