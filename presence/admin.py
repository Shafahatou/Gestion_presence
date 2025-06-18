from django.contrib import admin
from .models import Presence

@admin.register(Presence)
class PresenceAdmin(admin.ModelAdmin):
    list_display = ('utilisateur', 'date', 'heure_arrivee', 'latitude', 'longitude')
    list_filter = ('date',)
    search_fields = ('utilisateur__email',)
    readonly_fields = ('date', 'heure_arrivee')
