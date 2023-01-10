from django.db import models


class Client(models.Model):
    class Profession(models.TextChoices):
        student = "etudiant",("etudiant")
        worker = "travailleur",("travailleur")

    name = models.CharField(max_length=155)
    phone = models.PositiveBigIntegerField()
    profession = models.CharField(max_length=155,choices=Profession.choices, default=Profession.student)
    quartier = models.CharField(max_length=155, blank=True, default='ndokoti')
    date_enregistrement = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=155)

    def __str__(self):
        return self.name


class Service(models.Model):
    name = models.CharField(max_length=155)
    prix = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name


class Commande(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='services_commandes')
    created_at = models.DateField(auto_now_add=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='client_commandes')

    def __str__(self):
        return f"command {self.id} of {self.client}"


class Prestation(models.Model):
    prestataire = models.CharField(max_length=155)
    done_at = models.DateField()
    amount = models.IntegerField(default=0)
    satisfaction = models.CharField(max_length=155, default='satisfait')
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='client_presta')
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='service_presta')

    def __str__(self):
        return f"prestation de {self.prestataire}"





