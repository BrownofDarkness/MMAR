from django.shortcuts import render, redirect
from .forms import Clientform, Serviceform
from django.views import View
from .models import Client, Service, Category


class Home(View):
    template_name = 'societe.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


class ClientView(View):
    template_name = 'client.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        return render(request, self.template_name)


class ServicesView(View):
    template_name = 'services.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        return render(request, self.template_name)


class MdService(View):
    template_name = 'modifierservice.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        return render(request, self.template_name)


class Newcommand(View):
    template_name = 'nouveau.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        return render(request, self.template_name)


class AccountView(View):
    template_name = 'compte.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        return render(request, self.template_name)

