from django.shortcuts import render, redirect
from .forms import Clientform, Serviceform
from django.views import View
from .models import Client, Service, Commande
from django.contrib import messages


class Home(View):
    template_name = 'societe.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


class ClientView(View):
    template_name = 'client.html'

    def get(self, request, *args, **kwargs):
        clients = Client.objects.all()
        return render(request, self.template_name, {'clients':clients})

    def post(self, request, *args, **kwargs):
        return render(request, self.template_name)


class ClientDetailView(View):
    template_name = 'detailsclient.html'

    def get(self, request, pk,*args, **kwargs):
        client = Client.objects.get(pk=pk)
        comandes = client.client_commandes
        context = {
            'client':client,
            'comandes': comandes
        }
        return render(request, self.template_name,context)

    def post(self, request, *args, **kwargs):
        return render(request, self.template_name)


class ServicesView(View):
    template_name = 'services.html'
    form_class = Serviceform

    def get(self, request, *args, **kwargs):
        queryset = Service.objects.all()
        return render(request, self.template_name, {'form': self.form_class(), 'services': queryset})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            form.save(request)
            return redirect('services')
        return render(request, self.template_name, {'form': form})


class MdService(View):
    template_name = 'modifierservice.html'
    form_class = Serviceform

    def get(self, request, my_id,*args, **kwargs):
        obj = Service.objects.get(id=my_id)
        form = self.form_class(request.POST or None, instance=obj)
        return render(request, self.template_name,{'form': form})

    def post(self, request, my_id,*args, **kwargs):
        obj = Service.objects.get(id=my_id)
        form = self.form_class(request.POST or None, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('services')
        return render(request, self.template_name, {'form': form})


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

