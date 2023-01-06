from django.urls import path, include
from .views import Home, ClientView, ServicesView, AccountView, MdService, Newcommand

urlpatterns = [
    path("", Home.as_view(), name="home"),
    path("client", ClientView.as_view(), name="client"),
    path('service', ServicesView.as_view(), name='services'),
    path('compte', AccountView.as_view(), name='compte'),
    path('md_service', MdService.as_view(), name='md_service'),
    path('new_command', Newcommand.as_view(), name='new_command'),
]