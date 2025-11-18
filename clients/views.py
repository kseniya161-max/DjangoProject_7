from django.core.checks import messages
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from clients.forms import MailingSendForm
from clients.models import Clients, Message, Mailing


class ClientListView(ListView):
    model = Clients
    template_name = 'clients_list.html'
    context_object_name = 'list_clients'


class ClientCreateView(CreateView):
    model = Clients
    template_name = 'clients_create.html'
    fields = ['name', 'email', 'comment']
    success_url = reverse_lazy('clients_list')


class ClientUpdateView(UpdateView):
    model = Clients
    template_name = 'clients_add.html'
    fields = ['name', 'email', 'comment']
    success_url = reverse_lazy('clients_list')


class ClientDeleteView(DeleteView):
    model = Clients
    template_name = 'clients_del.html'
    success_url = reverse_lazy('clients_list')


class MessageListView(ListView):
    model = Message
    template_name = 'message_list.html'
    context_object_name = 'list_messages'


class MessageCreateView(CreateView):
    model = Message
    template_name = 'message_create.html'
    fields = ['header', 'content']
    success_url = reverse_lazy('message_list')


class MessageUpdateView(UpdateView):
    model = Message
    template_name = 'message_add.html'
    fields = ['header', 'content']
    success_url = reverse_lazy('message_list')


class MessageDeleteView(DeleteView):
    model = Message
    template_name = 'message_delete.html'
    success_url = reverse_lazy('message_list')


class MailingListView(ListView):
    model = Mailing
    template_name = 'mailing_list.html'
    context_object_name = 'list_mailing'


class MailingCreateView(CreateView):
    model = Mailing
    template_name = 'mailing_create.html'
    fields = ['datetime', 'status', 'message', 'recipients']
    success_url = reverse_lazy('mailing_list')


class MailingUpdateView(UpdateView):
    model = Mailing
    template_name = 'mailing_add.html'
    fields = ['datetime', 'status', 'message', 'recipients']
    success_url = reverse_lazy('mailing_list')


class MailingDeleteView(DeleteView):
    model = Mailing
    template_name = 'mailing_delete.html'
    success_url = reverse_lazy('mailing_list')


class MailingSendView(CreateView):
    form_class = MailingSendForm
    template_name = 'mailing_send.html'
    success_url = reverse_lazy('mailing_list')


    def form_valid(self, form):
        mailing = form.save(commit=False)
        mailing.status = 'started'
        mailing.save()

        self.send_mailing(mailing)
        messages.success(self.request, 'Рассылка успешно отправлена')
        return super().form_valid(form)

    def send_mailing(self, mailing):
        for recipient in mailing.recipients.all():
            pass












