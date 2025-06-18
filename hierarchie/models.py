from django.db import models
from django.conf import settings

class Direction(models.Model):
    name = models.CharField("Nom de la direction", max_length=100)
    director = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL,
        null=True, blank=True, related_name="directions")

    def __str__(self):
        return self.name

class Departement(models.Model):
    name = models.CharField("Nom du département", max_length=100)
    chief = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL,
        null=True, blank=True, related_name="chief_departements")
    
    direction = models.ForeignKey(Direction, on_delete=models.CASCADE, related_name="departements")

    def __str__(self):
        return self.name

class Service(models.Model):
    name = models.CharField("Nom du service", max_length=100)
    chief = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL,
        null=True, blank=True, related_name="chief_services")
    
    departement = models.ForeignKey(Departement, on_delete=models.CASCADE, related_name="services")
    employees = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="employees_services", blank=True)

    def __str__(self):
        return self.name

class Unite(models.Model):
    name = models.CharField("Nom de l’unité", max_length=100)
    chief = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL,
        null=True, blank=True, related_name="unites")
    
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name="unites")
    employees = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="employees_unites", blank=True)

    def __str__(self):
        return self.name
