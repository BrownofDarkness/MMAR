from django import forms
from .models import Client, Service, Prestation, Category
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

    class Meta:
        model = Service
        fields = ['name','prix', 'category']



class Categoryform(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']


class Prestationform(forms.ModelForm):
    class Meta:
        model = Prestation
        fields = ['client', 'service', 'prestataire', 'done_at', 'amount']

    def save(self, commit=True):
        pass
