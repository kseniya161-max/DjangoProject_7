from django.contrib import messages
from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.template.loader import render_to_string
from django.utils.crypto import get_random_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.views.generic import CreateView
from itsdangerous import URLSafeTimedSerializer
from Users.forms import UserRegisterForm
from Users.models import User
from config import settings
from django.core.mail import send_mail


class CreateUserView(CreateView):
    """Создаем представление для регистрации"""
    model = User
    form_class = UserRegisterForm
    template_name = 'register.html'
    success_url = reverse_lazy('Users:login')

    def form_valid(self, form):
        user = form.save()
        self.send_confirmation_email(user)
        messages.success(self.request, 'Ваш аккаунт был успешно создан! Проверьте Вашу почту для подтверждения.')
        return super().form_valid(form)

    def send_confirmation_email(self, user):
        """Отправка письма для Подтверждение Email"""
        s = URLSafeTimedSerializer(settings.SECRET_KEY)
        token = s.dumps(user.email, salt='email-confirmation')
        uid = urlsafe_base64_encode(force_bytes(user.pk))
        confirmation_link = f"http://localhost:8000/confirm/{uid}/{token}/"
        subject = 'Подтверждение email'
        message = render_to_string('email_confirmation.html', {
            'confirmation_link': confirmation_link,
        })
        send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [user.email])

User = get_user_model()

def confirm_email(request, uidb64, token):
    """Подтверждение Email"""
    try:
        s = URLSafeTimedSerializer(settings.SECRET_KEY)
        email = s.loads(token, salt='email-confirmation', max_age=3600)
        uid = urlsafe_base64_decode(uidb64).decode()
        user = User.objects.get(pk=uid)
        if user.email == email:
            user.email_verified = True
            user.save()
            messages.success(request, 'Ваш email был успешно подтвержден!')
            return redirect('Users:login')
    except Exception as e:
        messages.error(request, 'Ссылка для подтверждения недействительна или истекла.')
    return redirect('Users:register')







