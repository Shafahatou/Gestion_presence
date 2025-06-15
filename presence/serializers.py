from rest_framework import serializers
from .models import Presence

class PresenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Presence
        fields = ['id', 'date', 'heure_arrivee', 'latitude', 'longitude']
        read_only_fields = ['id', 'date', 'heure_arrivee']
