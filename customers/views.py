from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy

from customers.forms import CustomerForm
from customers.models import Customer


class CustomerListView(ListView):
    """Контроллер создания клиента сервиса"""
    model = Customer
    paginate_by = 15
    ordering = ['-id']


class CustomerCreateView(CreateView):
    """Контроллер просмотра списка клиентов сервиса"""
    model = Customer
    form_class = CustomerForm
    success_url = reverse_lazy('customers:customer_list')


class CustomerDetailView(DetailView):
    """Контроллер просмотра отдельного клиента сервиса"""
    model = Customer


class CustomerUpdateView(UpdateView):
    """Контроллер редактирования клиента сервиса"""
    model = Customer
    form_class = CustomerForm
    success_url = reverse_lazy('customers:customer_list')


class CustomerDeleteView(DeleteView):
    """Контроллер удаления клиента сервиса"""
    model = Customer
    success_url = reverse_lazy('customer:customer_list')
