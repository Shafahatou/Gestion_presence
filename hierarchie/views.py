from rest_framework import generics, permissions
from .models import Direction, Departement, Service, Unite
from .serializers import DirectionSerializer, DepartementSerializer, ServiceSerializer, UniteSerializer
from authentification.permissions import IsRHUser  



class DirectionListCreateView(generics.ListCreateAPIView):
    queryset = Direction.objects.all()
    serializer_class = DirectionSerializer
    permission_classes = [permissions.IsAuthenticated, IsRHUser]

class DepartementListCreateView(generics.ListCreateAPIView):
    queryset = Departement.objects.all()
    serializer_class = DepartementSerializer
    permission_classes = [permissions.IsAuthenticated, IsRHUser]

class ServiceListCreateView(generics.ListCreateAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    permission_classes = [permissions.IsAuthenticated, IsRHUser]

class UniteListCreateView(generics.ListCreateAPIView):
    queryset = Unite.objects.all()
    serializer_class = UniteSerializer
    permission_classes = [permissions.IsAuthenticated, IsRHUser]
