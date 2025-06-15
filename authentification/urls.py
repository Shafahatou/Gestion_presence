from django.urls import path
from .views import *

urlpatterns = [
    path('login', LoginView.as_view(), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('user', UtilisateurProfileView.as_view(), name='utilisateur'),
    path('register', RegisterView.as_view(), name='register'),
    path('refresh-token', TokenRefreshView.as_view(), name='token_refresh'),
    path('roles', RoleListView.as_view(), name='roles'),
]
