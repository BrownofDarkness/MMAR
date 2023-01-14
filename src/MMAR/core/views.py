from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .forms import Clientform, Serviceform
from django.views import View
from .models import Client, Service, Prestation, Category
from django.utils.decorators import method_decorator
from django.contrib.auth import get_user_model, authenticate, logout, login

from .filters import ClientFilterSearch

User = get_user_model()

"""class Home(View):
    template_name = 'homepage.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)"""


@method_decorator(login_required(login_url='login'), name='get')
class PrestationView(View):
    template_name = 'prestation.html'

    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        services=Service.objects.all()
        clients = Client.objects.all()
        client_search = None
        service_search = None
        payed = False
        name1 = self.request.GET.get('client_search')
        if name1:
            client_search = clients.filter(name=name1).first()
            if (client_search.client_presta.count() % 6) == 0 and client_search.client_presta.count() > 0 and client_search.profession == 'etudiant':
                payed = True
        name2 = self.request.GET.get('service_search')
        if name2:
            service_search = services.filter(name=name2).first()
        context = {
            'clients': clients.order_by('name'),
            'services': services,
            'client': client_search,
            'service': service_search,
            'payed': payed
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        prestataire = request.POST['prestateur']
        client = request.POST['nom_client']
        service = request.POST['nom_service']
        satisf = request.POST['satisfaction']
        day = request.POST['date']
        client = Client.objects.get(name=client)
        if not ((client.client_presta.count() % 6) == 0 and client.client_presta.count() > 0 and client.profession == 'etudiant'):
            amount = request.POST['amount']
        else:
            amount = 0
        service = Service.objects.get(name=service)
        prestation = Prestation.objects.create(prestataire=prestataire, done_at=day, amount=amount, satisfaction=satisf, client=client, service=service)
        return redirect('prestation')


@method_decorator(login_required(login_url='login'), name='get')
class SocieteView(View):
    template_name = 'societe.html'

    def get(self, request, *args, **kwargs):
        services_count = Service.objects.all().count()
        client_count = Client.objects.all().count()
        context = {
            'clients': client_count,
            'services': services_count
        }
        return render(request, self.template_name, context)


class LoginView(View):
    template_name = 'connexion.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('societe')
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        username = request.POST['nom']
        password = request.POST['psw']
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_active:
            login(request, user)
            return redirect('societe')
        return render(request, self.template_name)


@method_decorator(login_required(login_url='login'), name='get')
class ClientView(View):
    template_name = 'client.html'
    form_class = Clientform

    def get(self, request, *args, **kwargs):
        clients = Client.objects.all().order_by('-id')

        name = self.request.GET.get('client')
        if name:
            clients = clients.filter(name__icontains=name)

        liste = []

        for item in clients:
            clientset = {'client': item, 'last_command': '', 'frequence': 0}
            prestations = Prestation.objects.filter(client=item)
            if prestations:
                prestation = prestations.last()
                clientset['last_command'] = prestations.last()
                clientset['frequence'] = prestations.count()

            liste.append(clientset)
        return render(request, self.template_name, {'clients': liste, 'form': self.form_class()})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('client')
        return render(request, self.template_name, {'form': form})


@method_decorator(login_required(login_url='login'), name='get')
class ClientDetailView(View):
    template_name = 'detailsclient.html'

    def get(self, request, pk, *args, **kwargs):
        client = Client.objects.get(pk=pk)
        comandes = Prestation.objects.filter(client=client.id)
        context = {
            'client': client,
            'comandes': comandes.order_by('-id'),
            'compte': comandes.count()

        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        return render(request, self.template_name)


@method_decorator(login_required(login_url='login'), name='get')
class ClientDeleteView(View):
    template_name = 'pagesupprimer.html'

    def get(self, request, pk, *args, **kwargs):
        client = Client.objects.get(pk=pk)
        context = {
            'client': client,
        }
        return render(request, self.template_name, context)

    def post(self, request, pk, *args, **kwargs):
        obj = get_object_or_404(Client, pk=pk)
        obj.delete()
        return redirect('client')


@method_decorator(login_required(login_url='login'), name='get')
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


@method_decorator(login_required(login_url='login'), name='get')
class MdService(View):
    template_name = 'modifierservice.html'
    form_class = Serviceform

    def get(self, request, my_id, *args, **kwargs):
        obj = Service.objects.get(id=my_id)
        form = self.form_class(request.POST or None, instance=obj)
        return render(request, self.template_name, {'form': form})

    def post(self, request, my_id, *args, **kwargs):
        obj = Service.objects.get(id=my_id)
        form = self.form_class(request.POST or None, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('services')
        return render(request, self.template_name, {'form': form})


@method_decorator(login_required(login_url='login'), name='get')
class AccountView(View):
    template_name = 'compte.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        return render(request, self.template_name)


@method_decorator(login_required(login_url='login'), name='get')
class CategoryView(View):
    template_name = 'categorie.html'

    def get(self, request, *args, **kwargs):
        categories = Category.objects.all()
        return render(request, self.template_name, {'categories':categories})

    def post(self, request, *args, **kwargs):
        name = request.POST['name']
        categ = Category.objects.create(name=name)

        return redirect('category')


@method_decorator(login_required(login_url='login'), name='get')
class LogoutView(View):

    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('login')
