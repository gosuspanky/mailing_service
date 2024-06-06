from django.views.generic import TemplateView, CreateView, ListView, DetailView, UpdateView, DeleteView

from mailing.models import Mailing
from django.urls import reverse_lazy
from mailing.forms import MailingForm


class HomeView(TemplateView):
    """Контроллер просмотра домашней страницы"""
    template_name = "mailing/home.html"


class MailingCreateView(CreateView):
    """Контроллер создания рассылки"""
    model = Mailing
    form_class = MailingForm
    success_url = reverse_lazy('mailing:mailing_list')


class MailingListView(ListView):
    """Контроллер просмотра списка рассылок"""
    model = Mailing
    paginate_by = 9  # количество элементов на одну страницу
    ordering = ['-id']


class MailingDetailView(DetailView):
    """Контроллер просмотра отдельной рассылки"""
    model = Mailing


class MailingUpdateView(UpdateView):
    """Контроллер редактирования рассылки"""
    model = Mailing
    form_class = MailingForm
    success_url = reverse_lazy('mailing:mailing_list')


class MailingDeleteView(DeleteView):
    """Контроллер удаления рассылки"""
    model = Mailing
    success_url = reverse_lazy('mailing:mailing_list')
