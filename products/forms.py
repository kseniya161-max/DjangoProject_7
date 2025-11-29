from django.forms import ModelForm

from products.models import Category


class CategoryForm(ModelForm):
    """ Форма Создания Категории"""
    class Meta:
        model = Category
        fields = ['name', 'photo']

    def __init__(self, *args, **kwargs):
        super(CategoryForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Введите название категории'})
        self.fields['photo'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Фото'})
