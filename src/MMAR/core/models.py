from django.db import models


class Client(models.Model):
    class Profession(models.TextChoices):
        student = "etudiant",("etidiant")
        worker = "travailleur",("travailleur")

    name = models.CharField(max_length=155)
    phone = models.PositiveBigIntegerField()
    profession = models.CharField(max_length=155,choices=Profession.choices, default=Profession.student)
    date_enregistrement = models.DateField(auto_now_add=True)


class Service(models.Model):
    name = models.CharField(max_length=155)
    description = models.TextField()
    prix = models.IntegerField()


class Commande(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='services_commandes')
    client = models.OneToOneField(Client, on_delete=models.CASCADE, related_name='client_commandes')
    date = models.DateField(auto_now_add=True)





