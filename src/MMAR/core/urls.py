from django.urls import path, include
from .views import Home, ClientView, ServicesView, AccountView, MdService, Newcommand, ClientDetailView, SocieteView

urlpatterns = [
    path("", Home.as_view(), name="home"),
    path("dashbord/", SocieteView.as_view(), name="societe"),
    path("dashbord/client", ClientView.as_view(), name="client"),
    path('dashbord/service', ServicesView.as_view(), name='services'),
    path('dashbord/compte', AccountView.as_view(), name='compte'),
    path('dashbord/md_service/<int:my_id>/', MdService.as_view(), name='md_service'),
    path('dashbord/client/<int:pk>/', ClientDetailView.as_view(), name='client_detail'),
    path('dashbord/new_command', Newcommand.as_view(), name='new_command'),
]