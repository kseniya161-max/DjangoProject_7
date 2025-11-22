from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView

from clients.forms import MailingSendForm, ClientForm, MessageForm
from clients.models import Clients, Message, Mailing, MailingAttempt
from config.settings import DEFAULT_FROM_EMAIL


class ClientListView(ListView):
    model = Clients
    template_name = 'client_list.html'
    context_object_name = 'list_clients'


class ClientCreateView(CreateView):
    model = Clients
    form_class = ClientForm
    template_name = 'client_create.html'
    success_url = reverse_lazy('clients:client_list')


class ClientUpdateView(UpdateView):
    model = Clients
    form_class = ClientForm
    template_name = 'client_edit.html'
    success_url = reverse_lazy('clients:client_list')


class ClientDeleteView(DeleteView):
    model = Clients
    template_name = 'client_delete.html'
    success_url = reverse_lazy('clients:client_list')


class MessageListView(ListView):
    model = Message
    template_name = 'message_list.html'
    context_object_name = 'list_messages'


class MessageCreateView(CreateView):
    model = Message
    form_class = MessageForm
    template_name = 'message_create.html'
    success_url = reverse_lazy('clients:message_list')


class MessageUpdateView(UpdateView):
    model = Message
    template_name = 'message_update.html'
    fields = ['header', 'content']
    success_url = reverse_lazy('clients:message_list')


class MessageDeleteView(DeleteView):
    model = Message
    template_name = 'message_delete.html'
    success_url = reverse_lazy('clients:message_list')


class MailingListView(ListView):
    model = Mailing
    template_name = 'mailing_list.html'
    context_object_name = 'list_mailing'


class MailingCreateView(CreateView):
    model = Mailing
    form_class = MailingSendForm
    template_name = 'mailing_create.html'
    success_url = reverse_lazy('clients:mailing_list')

    def form_valid(self, form):
        if form.is_valid():
            return super().form_valid(form)
        else:
            print(form.errors)
            return self.form_invalid(form)



class MailingUpdateView(UpdateView):
    model = Mailing
    form_class = MailingSendForm
    template_name = 'mailing_update.html'
    success_url = reverse_lazy('clients:mailing_list')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['instance'] = self.get_object()
        return kwargs

    def form_valid(self, form):
        if form.is_valid():
            return super().form_valid(form)
        else:
            print(form.errors)
            return self.form_invalid(form)


class MailingDeleteView(DeleteView):
    model = Mailing
    template_name = 'mailing_delete.html'
    success_url = reverse_lazy('clients:mailing_list')



class MailingSendView(CreateView):
    form_class = MailingSendForm
    template_name = 'mailing_send.html'
    success_url = reverse_lazy('clients:mailing_list')


    def form_valid(self, form):
        mailing = form.save(commit=False)
        mailing.status = 'started'
        mailing.save()
        try:

            send_mail(
                'Тестовое письмо',
                'Это тестовое письмо от Django.',
                DEFAULT_FROM_EMAIL,
                ['baharevak161@gmail.com'],
                fail_silently=True,
            )
        except Exception as e:
            messages.error(self.request, f'Ошибка отправки тестового письма: {e}')
            return super().form_invalid(form)

        self.send_mailing(mailing)
        mailing.status = 'completed'
        mailing.save()

        messages.success(self.request, 'Рассылка успешно отправлена')
        return super().form_valid(form)

    def send_mailing(self, mailing):
        for recipient in mailing.recipients.all():
            try:
                send_mail(
                    mailing.message.header,
                    mailing.message.content,
                    DEFAULT_FROM_EMAIL,
                    [recipient.email],
                    fail_silently=False,
                )
                MailingAttempt.objects.create(
                    mailing=mailing,
                    status='success',
                    server_response='Письмо успешно отправлено'
                )
            except Exception as e:
                MailingAttempt.objects.create(
                    mailing=mailing,
                    status='failed',
                    server_response=str(e)
                )
class HomePageView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['total_mailing'] = Mailing.objects.count()
        context['active_mailing'] = Mailing.objects.filter(status='started').count()
        context['unique_recipients'] = Clients.objects.count()
        return context










