from django.contrib import admin
from .models import Utilisateur 

class UtilisateurAdmin(admin.ModelAdmin):
    pass

admin.site.register(Utilisateur, UtilisateurAdmin)
