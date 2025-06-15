from rest_framework import serializers
from .models import PermissionRequest

class PermissionRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = PermissionRequest
        fields = ['id', 'user', 'date_requested', 'start_date', 'end_date', 'reason', 'status']
        read_only_fields = ['id', 'user', 'date_requested', 'status']
