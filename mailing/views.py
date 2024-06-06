from django.views.generic import TemplateView, CreateView, ListView, DetailView, UpdateView, DeleteView

from mailing.models import Mailing, Log
from django.urls import reverse_lazy
from mailing.forms import MailingForm

from django.shortcuts import redirect


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


class LogListView(ListView):
    """Контроллер просмотра логов"""
    model = Log
    paginate_by = 9  # количество элементов на одну страницу

    def dispatch(self, request, *args, **kwargs):  # запрет доступа без авторизации
        if self.request.user.is_anonymous:
            return redirect('mailing:access_error')
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, *args, **kwargs):  # отображение логов только тех рассылок, которые созданы пользователем
        context_data = super().get_context_data(**kwargs)
        obj_lst = []
        for log in Log.objects.all():
            if log.mailing.created_by == self.request.user or self.request.user.is_manager:  # менеджеру доступны все логи
                obj_lst.append(log)
        obj_lst.reverse()
        context_data['object_list'] = obj_lst
        return context_data


class LogDetailView(DetailView):
    """Контроллер просмотра отдельного лога"""
    model = Log

    def dispatch(self, request, *args, **kwargs):  # доступ к логу только по рассылке, которая создана пользователем
        obj = self.get_object()
        if (obj.mailing.created_by != request.user) and (not self.request.user.is_manager):  # менеджеру доступны все логи
            return redirect('mailing:access_error')
        return super().dispatch(request, *args, **kwargs)


class AccessErrorView(TemplateView):
    """Контроллер ошибки доступа"""
    template_name = 'mailing/access_error.html'
