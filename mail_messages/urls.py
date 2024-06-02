from django.urls import path

from mail_messages.views import MessagesListView

app_name = 'mail_messages'

urlpatterns = [
    path('list/', MessagesListView.as_view(), name='messages_list'),
]
