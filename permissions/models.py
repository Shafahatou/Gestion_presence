from django.db import models
from django.conf import settings
from django.core.exceptions import ValidationError

class PermissionRequest(models.Model):
    STATUS_CHOICES = (
        ('PENDING', 'En attente'),
        ('APPROVED', 'Validée'),
        ('DENIED', 'Refusée'),
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="permission_requests")
    date_requested = models.DateTimeField(auto_now_add=True)
    start_date = models.DateField()
    end_date = models.DateField()
    reason = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='PENDING')

    reviewed_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, related_name='reviewed_permission_requests')
    review_date = models.DateTimeField(null=True, blank=True, auto_now=True)
    review_comment = models.TextField(blank=True, null=True)

    def clean(self):
        if self.end_date < self.start_date:
            raise ValidationError("La date de fin ne peut pas être avant la date de début.")

    def __str__(self):
        return f"Demande de permission de {self.user.email} du {self.start_date} au {self.end_date} - {self.status}"