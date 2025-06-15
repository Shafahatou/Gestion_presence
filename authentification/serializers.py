from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

Utilisateur = get_user_model()

class LoginSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, utilisateur):
        token = super().get_token(utilisateur)
        token['role'] = utilisateur.role
        return token

class UtilisateurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Utilisateur
        # Retirer 'username' si ce champ n'existe pas dans ton modèle
        fields = ['id', 'email', 'role']  # adapte ici selon tes champs exacts

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Utilisateur
        # Retirer 'username' si ce champ n'existe pas dans ton modèle
        fields = ['email', 'password', 'role']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        utilisateur = Utilisateur.objects.create_user(**validated_data)
        return utilisateur
