from django.contrib import admin
from  .models import PermissionRequest

class PermissionRequestAdmin(admin.ModelAdmin):
    pass

admin.site.register(PermissionRequest, PermissionRequestAdmin)

