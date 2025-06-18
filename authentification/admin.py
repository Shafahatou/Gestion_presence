from django.contrib import admin
from django.utils.html import format_html
from django.contrib.auth.admin import UserAdmin
from .models import Utilisateur


@admin.register(Utilisateur)
class UtilisateurAdmin(UserAdmin):
    model = Utilisateur
    list_display = (
        'id', 'clickable_email', 'first_name', 'last_name',
        'role', 'sex', 'get_direction', 'get_departement', 'get_service', 'get_unite',
        'is_active', 'is_staff'
    )
    list_filter = ('role', 'sex', 'is_active', 'is_staff')
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('email',)

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ("Informations personnelles", {
            'fields': (
                'first_name', 'last_name', 'sex', 'role',
                'get_direction', 'get_departement', 'get_service', 'get_unite'
            )
        }),
        ("Permissions", {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ("Dates importantes", {'fields': ('last_login',)}),
    )

    readonly_fields = ('get_direction', 'get_departement', 'get_service', 'get_unite')

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'email', 'first_name', 'last_name', 'sex', 'role',
                'password1', 'password2', 'is_staff', 'is_superuser'
            ),
        }),
    )

    @admin.display(description="Email")
    def clickable_email(self, obj):
        return format_html('<a href="mailto:{}">{}</a>', obj.email, obj.email)

    @admin.display(description="Direction")
    def get_direction(self, obj):
        d = getattr(obj, "directions", None)
        return d.first().name if d and d.exists() else "—"

    @admin.display(description="Département")
    def get_departement(self, obj):
        d = getattr(obj, "chief_departements", None)
        return d.first().name if d and d.exists() else "—"

    @admin.display(description="Service")
    def get_service(self, obj):
        if obj.services_employe.exists():
            return ", ".join([s.name for s in obj.services_employe.all()])
        s = getattr(obj, "chief_services", None)
        return s.first().name if s and s.exists() else "—"

    @admin.display(description="Unités")
    def get_unite(self, obj):
        return ", ".join([u.name for u in obj.unites_employe]) if obj.unites_employe else "—"



    # @admin.display(description="Départements")
    # def list_departements(self, obj):
    #     return ", ".join([d.name for d in obj.departements.all()])

    # @admin.display(description="Services")
    # def list_services(self, obj):
    #     return ", ".join([s.name for s in obj.services.all()])