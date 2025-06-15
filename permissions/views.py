from django.shortcuts import render
from rest_framework import generics, permissions
from .models import PermissionRequest
from .serializers import PermissionRequestSerializer

class PermissionRequestCreateView(generics.CreateAPIView):
    serializer_class = PermissionRequestSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class MyPermissionsListView(generics.ListAPIView):
    serializer_class = PermissionRequestSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return PermissionRequest.objects.filter(user=self.request.user).order_by('-date_requested')
