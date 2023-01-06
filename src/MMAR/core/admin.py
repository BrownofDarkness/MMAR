from django.contrib import admin
from .models import Client, Service,Commande
# Register your models here.


class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'profession', 'date_enregistrement')


class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'prix', 'description')


admin.site.register(Client, ClientAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Commande)