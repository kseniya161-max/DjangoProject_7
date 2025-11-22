from django.contrib import messages
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from Users.forms import UserRegisterForm
from Users.models import User


class CreateUserView(CreateView):
    """Создаем представление для регистрации"""
    model = User
    form_class = UserRegisterForm
    template_name = 'register.html'
    success_url = reverse_lazy('Users:register')

    def form_valid(self, form):
        messages.success(self.request, 'Ваш аккаунт был успешно создан! Теперь Вы можете войти.')
        return super().form_valid(form)


