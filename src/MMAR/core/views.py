from django.shortcuts import render, redirect
from .forms import Clientform, Serviceform,Commandform
from django.views import View
from .models import Client, Service, Commande
from django.contrib import messages


class Home(View):
    template_name = 'homepage.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


class SocieteView(View):
    template_name = 'societe.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


class LoginView(View):
    template_name = 'connexion.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


class ClientView(View):
    template_name = 'client.html'
    form_class = Clientform

    def get(self, request, *args, **kwargs):
        clients = Client.objects.all().order_by('-id')
        list =[]

        for item in clients:
            clientview = {'client': item, 'last_command': '', 'frequence': 0}
            if Commande.objects.filter(client=item):
                commande =Commande.objects.filter(client=item).last()
                print(commande)
                clientview['last_command'] = Commande.objects.filter(client=item).last()
                clientview['frequence'] = Commande.objects.filter(client=item).count()

            list.append(clientview)
        return render(request, self.template_name, {'clients': list, 'form': self.form_class()})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('services')
        return render(request, self.template_name, {'form': form})


class ClientDetailView(View):
    template_name = 'detailsclient.html'

    def get(self, request, pk,*args, **kwargs):
        client = Client.objects.get(pk=pk)
        comandes = Commande.objects.filter(client=client.id)
        context = {
            'client': client,
            'comandes': comandes.order_by('-id'),
            'compte': comandes.count()

        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        return render(request, self.template_name)


class ServicesView(View):
    template_name = 'services.html'
    form_class = Serviceform

    def get(self, request, *args, **kwargs):
        queryset = Service.objects.all().order_by('-id')
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
            return redirect('clients')
        return render(request, self.template_name, {'form': form})


class Newcommand(View):
    template_name = 'nouveau.html'
    form_class = Commandform

    def get(self, request,pk, *args, **kwargs):
        return render(request, self.template_name, {'form': self.form_class()})

    def post(self, request, pk, *args, **kwargs):
        form = self.form_class(request.POST or None)
        if form.is_valid():
            form.save(pk)
            return redirect('client')
        return render(request, self.template_name, {'form': form})


class AccountView(View):
    template_name = 'compte.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        return render(request, self.template_name)

