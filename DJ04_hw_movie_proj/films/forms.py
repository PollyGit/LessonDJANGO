from django.forms import ModelForm, TextInput, DateTimeInput, Textarea

# импорт таблицы
from .models import Films_post


# Прописываем новый класс с названием, как у таблицы+слово Form
class Films_postForm(ModelForm):
    class Meta:
        model = Films_post
        # Поля у формы
        fields = ['title', 'short_description', 'text']
        # Создаём специальный виджет, в котором будем хранить словарь
        # Указываем атрибуты: тип и класс берем из page2.html
        widgets = {
            'title': TextInput(attrs={'class': 'form-control', 'placeholder': 'Название фильма'}),
            'short_description': Textarea(attrs={'class': 'form-control', 'placeholder': 'Описание фильма'}),
            'text': Textarea(attrs={'class': 'form-control', 'placeholder': 'Отзыв'}),
        }
