from django.db import models

# Create your models here.

# Создать класс для работы с БД
# models.Model - название класса от кот-го наследуется
class News_post(models.Model):
    title = models.CharField('Название новости', max_length=50)
    short_description = models.CharField('Краткое описание новости', max_length=200)
    text = models.TextField('Новость')
    pub_date = models.DateTimeField('Дата публикации')
    #user_post = models.CharField('Чья новость', max_length=50)
    #data = models.DateTimeField('Дата')


    #прописываем специальный метод внутри класса,
    # чтобы на сайте отображалось название новости.
    def __str__(self):
        return self.title


    #создаём вложенный класс Meta,
    # чтобы дать русские названия таблице News_post
    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
