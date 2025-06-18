from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.db import models

class UtilisateurManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("L'utilisateur doit avoir un email")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)


class Utilisateur(AbstractBaseUser, PermissionsMixin):
    ROLE_CHOICES = (
        ('RH', 'Ressources Humaines'),
        ('DIRECTOR', 'Directeur'),
        ('EMPLOYEE', 'Employé'),
    )
    SEX_CHOICES = (
        ('F', 'Féminin'),
        ('M', 'Masculin'),
    )

    email = models.EmailField(unique=True)
    first_name = models.CharField("Prénom", max_length=100, null=True, blank=True)
    last_name = models.CharField("Nom", max_length=100, null=True, blank=True)
    sex = models.CharField("Sexe", max_length=1, choices=SEX_CHOICES, default='F')
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='EMPLOYEE')


    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = UtilisateurManager()

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.email})"
    

    @property
    def direction_dirigee(self):
        return getattr(self, "directions", None).first()

    @property
    def departement_chef(self):
        return getattr(self, "chief_departements", None).first()

    @property
    def service_chef(self):
        return getattr(self, "chief_services", None).first()

    @property
    def unite_chef(self):
        return getattr(self, "unites", None).first()

    @property
    def services_employe(self):
        return self.employees_services.all()

    @property
    def unites_employe(self):
        return self.employees_unites.all()

