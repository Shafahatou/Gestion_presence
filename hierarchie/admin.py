from django.contrib import admin
from .models import Direction, Departement, Service, Unite

@admin.register(Direction)
class DirectionAdmin(admin.ModelAdmin):
    list_display = ('name', 'director')
    search_fields = ('name', 'director__email')

@admin.register(Departement)
class DepartementAdmin(admin.ModelAdmin):
    list_display = ('name', 'chief', 'direction')
    list_filter = ('direction',)
    search_fields = ('name', 'chief__email', 'direction__name')

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'chief', 'departement')
    list_filter = ('departement',)
    search_fields = ('name', 'chief__email', 'departement__name')
    filter_horizontal = ('employees',)

@admin.register(Unite)
class UniteAdmin(admin.ModelAdmin):
    list_display = ('name', 'chief', 'service')
    list_filter = ('service',)
    search_fields = ('name', 'chief__email', 'service__name')
    filter_horizontal = ('employees',)
