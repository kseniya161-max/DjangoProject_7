from django.contrib.admin import views
from django.urls import path, include


from config.clients.views import ClientListView, ClientCreateView, ClientUpdateView, ClientDeleteView, MessageListView, MessageCreateView, MessageUpdateView,MessageDeleteView

app_name = "clients"

urlpatterns = [
    path('', ClientListView.as_view(), name='client_list'),
    path('client/add/', ClientCreateView.as_view(), name='client_add'),
    path('client/<int:pk>/edit/', ClientUpdateView.as_view(), name='client_update'),
    path('client/<int:pk>/delete/', ClientDeleteView.as_view(), name='client_delete'),
    path('message/', MessageListView.as_view(), name='message_list'),
    path('message/add/', MessageCreateView.as_view(), name='message_add'),
    path('message/<int:pk>/edit/', MessageUpdateView.as_view(), name='message_update'),
    path('message/<int:pk>/delete/', MessageDeleteView.as_view(), name='message_delete'),
]