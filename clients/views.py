from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from config.clients.models import Clients, Message


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


class MessageCreateView(CreateView):
    model = Message
    template_name = 'message_create.html'
    fields = ['header', 'content']
    success_url = reverse_lazy('message_list')


class MessageUpdateView(CreateView):
    model = Message
    template_name = 'message_add.html'
    fields = ['header', 'content']
    success_url = reverse_lazy('message_list')


class MessageDeleteView(DeleteView):
    model = Message
    template_name = 'message_delete.html'
    success_url = reverse_lazy('message_list')















