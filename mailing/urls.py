from django.urls import path

from mailing.views import HomeView, MailingListView, MailingCreateView, MailingDetailView, MailingUpdateView, \
    MailingDeleteView

app_name = 'mailing'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),

    path('list/', MailingListView.as_view(), name='mailing_list'),
    path('create/', MailingCreateView.as_view(), name='mailing_create'),
    path('view/<int:pk>/', MailingDetailView.as_view(), name='mailing_detail'),
    path('edit/<int:pk>/', MailingUpdateView.as_view(), name='mailing_edit'),
    path('delete/<int:pk>/', MailingDeleteView.as_view(), name='mailing_delete'),
]
