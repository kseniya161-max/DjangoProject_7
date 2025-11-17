from django.forms import ModelForm
from django.core.exceptions import ValidationError
from django import forms
from config. clients.models import Message, Clients



class ClientForm(ModelForm):
    """ Форма Создания клиента"""
    class Meta:
        model = Clients
        fields = ['email', 'name', 'comment']

    def __init__(self, *args, **kwargs):
        super(ClientForm, self).__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Введите email'})
        self.fields['name'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Введите Имя'})
        self.fields['comment'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Напишите комментарий'})


    def clean_email(self):
        """ Валидация email"""
        email = self.cleaned_data.get('email')
        if Clients.objects.filter(email=email).exists():
            raise ValidationError ('Пользовталь с таким email уже существует')
        return email


class MessageForm(ModelForm):
    """ Форма Создания сообщения"""

    class Meta:
        model = Message
        fields = ['header', 'content']

    def __init__(self, *args, **kwargs):
        super(MessageForm, self).__init__(*args, **kwargs)
        self.fields['header'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Введите Заголовок'})
        self.fields['content'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Введите Контент'})

