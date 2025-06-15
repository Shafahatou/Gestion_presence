from django.urls import path
from .views import ScanPresenceView, PresenceHistoryView

urlpatterns = [
    path('scan/', ScanPresenceView.as_view(), name='presence-scan'),
    path('history/', PresenceHistoryView.as_view(), name='presence-history'),
]
