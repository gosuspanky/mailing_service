from django.shortcuts import render
from django.views.generic import TemplateView


class HomeView(TemplateView):
    """Контроллер просмотра домашней страницы"""
    template_name = "mailing/home.html"
