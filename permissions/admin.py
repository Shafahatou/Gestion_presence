from django.contrib import admin
from django.utils import timezone
from .models import PermissionRequest

@admin.register(PermissionRequest)
class PermissionRequestAdmin(admin.ModelAdmin):
    list_display = (
        'user', 'start_date', 'end_date', 'status',
        'reviewed_by', 'date_requested'
    )
    list_filter = ('status', 'start_date', 'end_date')
    search_fields = ('user__email', 'reason')
    readonly_fields = ('date_requested',)

    actions = ['approve_permissions', 'deny_permissions']

    def approve_permissions(self, request, queryset):
        updated = queryset.filter(status='PENDING').update(
            status='APPROVED',
            reviewed_by=request.user,
            review_date=timezone.now()
        )
        self.message_user(request, f"{updated} demande(s) approuvée(s).")
    approve_permissions.short_description = "Approuver les permissions sélectionnées"

    def deny_permissions(self, request, queryset):
        updated = queryset.filter(status='PENDING').update(
            status='DENIED',
            reviewed_by=request.user,
            review_date=timezone.now()
        )
        self.message_user(request, f"{updated} demande(s) refusée(s).")
    deny_permissions.short_description = "Refuser les permissions sélectionnées"
