from django.urls import path, include
from .views import ClientView, ServicesView, AccountView, MdService, ClientDetailView, SocieteView, LoginView, ClientDeleteView, PrestationView, CategoryView, LogoutView

urlpatterns = [
    path("", LoginView.as_view(), name="login"),
    path("logout", LogoutView.as_view(), name="logout"),
    path("dashbord/", SocieteView.as_view(), name="societe"),
    path("dashbord/prestation", PrestationView.as_view(), name="prestation"),
    path("dashbord/client", ClientView.as_view(), name="client"),
    path('dashbord/service', ServicesView.as_view(), name='services'),
    path('dashbord/compte', AccountView.as_view(), name='compte'),
    path('dashbord/categorie', CategoryView.as_view(), name='category'),
    path('dashbord/md_service/<int:my_id>/', MdService.as_view(), name='md_service'),
    path('dashbord/client/<int:pk>/', ClientDetailView.as_view(), name='client_detail'),
    path('dashbord/client/<int:pk>/delete', ClientDeleteView.as_view(), name='delete_client'),
]