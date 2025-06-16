from django.shortcuts import render
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.contrib.auth import get_user_model
from .serializers import (
    LoginSerializer, UtilisateurSerializer, RegisterSerializer
)
from .permissions import IsRHUser  # 🔐 Import de la permission personnalisée

Utilisateur = get_user_model()

class LoginView(TokenObtainPairView):
    serializer_class = LoginSerializer

class LogoutView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        try:
            print(request.data)
            token = RefreshToken(request.data['refresh'])
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception:
            return Response(status=status.HTTP_400_BAD_REQUEST)

class UtilisateurProfileView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        serializer = UtilisateurSerializer(request.user)
        return Response(serializer.data)

class RegisterView(APIView):
    permission_classes = [permissions.IsAuthenticated, IsRHUser]  # RH uniquement

    def post(self, request, *args, **kwargs):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            utilisateur = serializer.save()
            return Response({
                "message": "Utilisateur inscrit avec succès.",
                "utilisateur": {
                    "id": utilisateur.id,
                    "email": utilisateur.email,
                    "role": utilisateur.role,
                }
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RoleListView(APIView):
    def get(self, request):
        return Response([
            {"code": "RH", "label": "Ressources Humaines"},
            {"code": "DIRECTOR", "label": "Directeur"},
            {"code": "EMPLOYEE", "label": "Employé"}
        ])
