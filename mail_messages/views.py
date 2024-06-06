from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from mail_messages.forms import MessageForm
from mail_messages.models import Message

from django.urls import reverse_lazy


class MessageListView(ListView):
    """Контроллер просмотра списка сообщений для рассылки"""
    model = Message
    paginate_by = 6
    ordering = ['-id']


class MessageCreateView(CreateView):
    """Контроллер создания сообщения для рассылки"""
    model = Message
    form_class = MessageForm
    success_url = reverse_lazy('mail_messages:message_list')


class MessageDetailView(DetailView):
    """Контроллер просмотра отдельного сообщения для рассылки"""
    model = Message


class MessageUpdateView(UpdateView):
    """Контроллер редактирования сообщения для рассылки"""
    model = Message
    form_class = MessageForm
    success_url = reverse_lazy('mail_messages:message_list')


class MessageDeleteView(DeleteView):
    """Контроллер удаления сообщения для рассылки"""
    model = Message
    success_url = reverse_lazy('mail_messages:message_list')
