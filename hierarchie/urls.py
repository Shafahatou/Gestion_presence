from django.urls import path
from .views import *

urlpatterns = [
    path('directions/', DirectionListCreateView.as_view(), name='directions'),
    path('departements/', DepartementListCreateView.as_view(), name='departements'),
    path('services/', ServiceListCreateView.as_view(), name='services'),
    path('unites/', UniteListCreateView.as_view(), name='unites'),
]
