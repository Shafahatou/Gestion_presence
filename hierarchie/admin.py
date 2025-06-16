from django.contrib import admin
from .models import Direction, Departement, Service, Unite


class DirectionAdmin(admin.ModelAdmin):
    pass
admin.site.register(Direction, DirectionAdmin)


class DepartementAdmin(admin.ModelAdmin):
    pass
admin.site.register(Departement, DepartementAdmin)


class ServiceAdmin(admin.ModelAdmin):
    pass
admin.site.register(Service, ServiceAdmin)


class UniteAdmin(admin.ModelAdmin):
    pass
admin.site.register(Unite, UniteAdmin)


