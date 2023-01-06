from django import forms
from .models import Client, Service, Commande


class Clientform(forms.ModelForm):

    class Meta:
        model = Client
        fields = ['name', 'phone', 'profession']


class Serviceform(forms.ModelForm):
    name = forms.CharField(label='Intitulé', max_length=155, required=True, widget=forms.TextInput())
    prix = forms.IntegerField(label='Prix', required=True, widget=forms.NumberInput())
    description = forms.CharField(label='Description', required=True, widget=forms.Textarea())

    class Meta:
        model = Service
        fields = ['name','description','prix']
