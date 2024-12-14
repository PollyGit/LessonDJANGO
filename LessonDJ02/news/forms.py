from django.forms import ModelForm, TextInput, DateTimeInput, Textarea

# импорт таблицы
from .models import News_post


# Прописываем новый класс с названием, как у таблицы+слово Form
class News_postForm(ModelForm):
    class Meta:
        model = News_post
        # Поля у формы
        fields = ['title', 'short_description', 'text', 'pub_date']
        # Создаём специальный виджет, в котором будем хранить словарь
        # Указываем атрибуты: тип и класс берем из add_new_post.html
        widgets = {
            'title': TextInput(attrs={'class': 'form-control', 'placeholder': 'Заголовок новости'}),
            'short_description': TextInput(attrs={'class': 'form-control', 'placeholder': 'Краткое описание новости'}),
            'text': Textarea(attrs={'class': 'form-control', 'placeholder': 'Содержание новости'}),
            'pub_date': DateTimeInput(attrs={'class': 'form-control', 'placeholder': 'Дата публикации'})
        }
