from django import forms
from .models import Client, Service, Commande
from django.contrib.auth import get_user_model

User = get_user_model()

class Clientform(forms.ModelForm):
    name = forms.CharField(label='Nom client', max_length=155, required=True, widget=forms.TextInput())
    quartier = forms.CharField(label='Quartier du client', max_length=155, required=True, widget=forms.TextInput())
    phone = forms.IntegerField(label='Telephone', required=True, widget=forms.NumberInput())

    class Meta:
        model = Client
        fields = ['name', 'quartier', 'phone', 'profession']



class Serviceform(forms.ModelForm):
    name = forms.CharField(label='Intitulé', max_length=155, required=True, widget=forms.TextInput())
    prix = forms.IntegerField(label='Prix', required=True, widget=forms.NumberInput())
    description = forms.CharField(label='Description', required=True, widget=forms.Textarea())

    class Meta:
        model = Service
        fields = ['name','description','prix']


class Commandform(forms.ModelForm):

    class Meta:
        model = Commande
        fields = ['service']

    def save(self,pk, commit=True):
        service = self.cleaned_data['service']
        client = Client.objects.get(pk=pk)
        commande = Commande.objects.create(service=service, client=client)

        return commande


