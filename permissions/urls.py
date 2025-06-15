from django.urls import path
from .views import PermissionRequestCreateView, MyPermissionsListView

urlpatterns = [
    path('request/', PermissionRequestCreateView.as_view(), name='permission-request'),
    path('my-requests/', MyPermissionsListView.as_view(), name='my-permissions-requests'),
]
