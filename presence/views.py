from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Presence
from .serializers import PresenceSerializer

class ScanPresenceView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        data = {
            "utilisateur": request.user.id,
            "latitude": request.data.get("latitude"),
            "longitude": request.data.get("longitude"),
        }
        serializer = PresenceSerializer(data=data)
        if serializer.is_valid():
            serializer.save(utilisateur=request.user)
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

class PresenceHistoryView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = PresenceSerializer

    def get_queryset(self):
        return Presence.objects.filter(utilisateur=self.request.user).order_by('-date')
