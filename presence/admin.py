from django.contrib import admin
from  .models import Presence

class PresenceAdmin(admin.ModelAdmin):
    pass

admin.site.register(Presence, PresenceAdmin)

