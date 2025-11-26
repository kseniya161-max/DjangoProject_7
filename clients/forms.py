from django.forms import ModelForm, forms
from django.core.exceptions import ValidationError
from clients.models import Message, Clients, Mailing
from django import forms



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


class MailingSendForm(forms.ModelForm):
    # mailing = forms.ModelChoiceField(queryset=Mailing.objects.all(), required=True)
    class Meta:
        model = Mailing
        fields=['recipients', 'message', 'status', 'datetime_start', 'datetime_end']


    def clean(self):
        cleaned_data = super().clean()
        print(cleaned_data)
        datetime_start = cleaned_data.get('datetime_start')
        datetime_end = cleaned_data.get('datetime_end')
        if datetime_start and datetime_end and  datetime_end < datetime_start:
            raise ValidationError('Дата завершения не может быть больше даты начала')
        return cleaned_data
