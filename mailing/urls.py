from django.urls import path

from mailing.views import HomeView

app_name = 'mailing'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
]
