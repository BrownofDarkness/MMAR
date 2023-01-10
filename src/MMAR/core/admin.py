from django.contrib import admin
from .models import Client, Service, Prestation, Category
# Register your models here.


class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'profession', 'date_enregistrement')


class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'prix')


class PrestationAdmin(admin.ModelAdmin):
    list_display = ('prestataire', 'client', 'service', 'amount', 'done_at')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','name')


admin.site.register(Client, ClientAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Prestation, PrestationAdmin)
admin.site.register(Category, CategoryAdmin)